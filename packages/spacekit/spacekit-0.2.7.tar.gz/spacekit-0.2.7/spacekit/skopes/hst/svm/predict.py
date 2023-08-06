import tensorflow as tf
import numpy as np
import pandas as pd
import argparse
import os
import sys
import datetime as dt
import importlib.resources
from spacekit.extractor.load import SVMImages

DIM = 3
CH = 3
SIZE = 128
DEPTH = DIM * CH
SHAPE = (DIM, SIZE, SIZE, CH)

TF_CPP_MIN_LOG_LEVEL = 2


def get_model(model_path=None):
    """Loads pretrained Keras functional model"""
    if model_path is None:
        with importlib.resources.path(
            "spacekit.skopes.trained_networks", "ensembleSVM"
        ) as M:
            model_path = M
    print("Loading saved model: ", model_path)
    model = tf.keras.models.load_model(model_path)
    return model


def load_regression_data(data_file):
    """Loads preprocessed regression test data from csv"""
    print("Loading regression test data for MLP")
    data = pd.read_csv(data_file, index_col="index")
    column_order = [
        "numexp",
        "rms_ra",
        "rms_dec",
        "nmatches",
        "point",
        "segment",
        "gaia",
        "det",
        "wcs",
        "cat",
    ]
    try:
        X_data = data[column_order]
        print("Input Shape: ", X_data.shape)
        return X_data
    except Exception as e:
        print(e)
        print("Dataframe must contain these columns: ", column_order)
        sys.exit(1)


def load_image_data(X_data, img_path, size=None):
    """Loads total detection png images and converts to arrays"""
    print("Loading images into arrays")
    if size is not None:
        SIZE = size
    else:
        SIZE = 128
    svm_img = SVMImages(img_path, SIZE, SIZE, DEPTH)
    idx, X_img = svm_img.detector_prediction_images(X_data, DIM)
    print("Inputs: ", X_img.shape[0])
    print("Dimensions: ", X_img.shape[1])
    print("Width: ", X_img.shape[2])
    print("Height: ", X_img.shape[3])
    print("Channels: ", X_img.shape[4])
    print("Input Shape: ", X_img.shape)
    return idx, X_img


def load_mixed_inputs(data_file, img_path, size=None):
    X_data = load_regression_data(data_file)
    idx, X_img = load_image_data(X_data, img_path, size=size)
    diff = X_data.shape[0] - X_img.shape[0]
    if diff > 0:
        X_data = X_data.loc[X_data.index.isin(idx)]
        print(f"{diff} missing images removed from index")
        print(f"X_data: {X_data.shape}\nX_img:  {X_img.shape}")
    return X_data, X_img


def make_ensemble_data(X_data, X_img):
    print("Joining regression data and image arrays")
    X = [X_data, X_img]
    return X


def classify_alignments(model, X):
    """Returns classifier predictions and probability scores"""
    proba = model.predict(X)
    y_pred = np.round(proba[:, 0]).reshape(-1, 1)
    y_proba = proba[:, 0].reshape(-1, 1)
    return y_pred, y_proba


def save_preds(X_data, y_pred, y_proba, output_path):
    preds = np.concatenate([y_pred, y_proba], axis=1)
    pred_proba = pd.DataFrame(preds, index=X_data.index, columns=["y_pred", "y_proba"])
    preds = X_data.join(pred_proba)
    preds["index"] = preds.index
    output_file = f"{output_path}/predictions.csv"
    preds.to_csv(output_file, index=False)
    print("Y_PRED + Probabilities added. Dataframe saved to: ", output_file)
    return preds


def classification_report(df, output_path):
    P, T = df["y_pred"], df["det"].value_counts()
    C = df.loc[P == 1.0]
    cmp = C["det"].value_counts()
    dets = ["HRC", "IR", "SBC", "UVIS", "WFC"]
    separator = "---" * 5
    out = sys.stdout
    with open(f"{output_path}/clf_report.txt", "w") as f:
        sys.stdout = f
        print("CLASSIFICATION REPORT - ", dt.datetime.now())
        print(separator)
        print("Mean Probability Score: ", df["y_proba"].mean())
        print("Standard Deviation: ", df["y_proba"].std())
        print(separator)
        print("Aligned ('0.0') vs Misaligned ('1.0')")
        cnt_pct = pd.concat(
            [P.value_counts(), P.value_counts(normalize=True)],
            axis=1,
            keys=["cnt", "pct"],
        )
        print(cnt_pct)
        print(separator)
        print("Misalignment counts by Detector")
        for i, d in enumerate(dets):
            if i in cmp:
                print(f"{d}\t{cmp[i]} \t ({T[i]}) \t {np.round((cmp[i]/T[i])*100, 1)}%")
            elif i in T:
                print(f"{d}\t0 \t ({T[i]}) \t 0%")
            else:
                print(f"{d}\t0 \t (0) \t 0%")
        sys.stdout = out
    print(f"\nClassification Report created: {output_path}/clf_report.txt")
    with open(f"{output_path}/compromised.txt", "w") as file:
        for line in list(C["y_pred"].index):
            file.writelines(f"{line}\n")
    print(f"\nSuspicious/Compromised List created: {output_path}/compromised.txt")


def predict_alignment(
    data_file, img_path, model_path=None, output_path=None, size=None
):
    ens_clf = get_model(model_path=model_path)
    X_data, X_img = load_mixed_inputs(data_file, img_path, size=size)
    X = make_ensemble_data(X_data, X_img)
    y_pred, y_proba = classify_alignments(ens_clf, X)
    if output_path is None:
        output_path = os.getcwd()
    output_path = os.path.join(output_path, "predictions")
    os.makedirs(output_path, exist_ok=True)
    preds = save_preds(X_data, y_pred, y_proba, output_path)
    classification_report(preds, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="spacekit",
        usage="spacekit.skopes.hst.svm.predict svm_data.csv img",
    )
    parser.add_argument(
        "data_file",
        type=str,
        default="svm_data.csv",
        help="path to preprocessed mosaic data csv file",
    )
    parser.add_argument("img_path", type=str, help="path to PNG mosaic images")
    parser.add_argument(
        "-m",
        "--model_path",
        type=str,
        default=None,
        help="saved model path",
    )
    parser.add_argument(
        "-o",
        "--output_path",
        type=str,
        default=None,
        help="location to store output files",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        default=None,
        help="image size (width and height). Default is None (128).",
    )
    args = parser.parse_args()
    data_file = args.data_file
    img_path = args.img_path
    model_path = args.model_path
    output_path = args.output_path
    size = args.size
    predict_alignment(
        data_file, img_path, model_path=model_path, output_path=output_path, size=size
    )
