"""
    Batch prediction script.

    This module:
    - Loads trained model
    - Loads blind test dataset
    - Generates predictions
    - Saves predictions in required CSV format
"""

import joblib
import pandas as pd
from config import *
from data import load_blind_data


def predict(input_path: str, output_path: str):
    """
        Generate predictions for blind dataset.

        Parameters
        ----------
        input_path : str
            Path to blind dataset.
        output_path : str
            Output CSV path for predictions.
    """

    # Load model and data:
    model = joblib.load(MODEL_PATH)
    x = load_blind_data(input_path)

    # Predict data with the model choosen:
    preds = model.predict(x)

    # Generate CSV with predictions:
    pd.DataFrame({"target_pred": preds}).to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    predict(TEST_DATA_PATH, RESULTS_DATA_PATH)