"""
    Training pipeline for regression model.

    Responsibilities:
    - Load data
    - Split data
    - Train model
    - Evaluate performance
    - Log experiment with MLflow
    - Save trained model locally
"""

import os
import joblib
import mlflow
import mlflow.sklearn
import numpy as np

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import mean_squared_error, r2_score

from config import *
from data import load_training_data


def build_model():
    """
        Factory method to build model based on configuration.

        Returns
        -------
        sklearn-like model
    """

    model_type = MODEL_CONFIG["model_type"]
    params = MODEL_CONFIG["params"]

    if model_type == "xgboost":
        from xgboost import XGBRegressor
        return XGBRegressor(**params)

    elif model_type == "lightgbm":
        from lightgbm import LGBMRegressor
        return LGBMRegressor(**params)

    elif model_type == "random_forest":
        from sklearn.ensemble import RandomForestRegressor
        return RandomForestRegressor(**params)

    else:
        raise ValueError(f"Unsupported model type: {model_type}")


# Train model:
def train(training_path: str):
    """
        Main training function.

        Parameters
        ----------
        training_path : str
            Path to training dataset.
    """

    # Create/Use experiment:
    mlflow.set_experiment(MLFLOW_EXPERIMENT)

    # Load and split data:
    x, y = load_training_data(training_path)
    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    # Everything registered as one run:
    with mlflow.start_run():
        
        # Create, train and predict with final selected model:
        model = build_model()
        model.fit(x_train, y_train)
        preds = model.predict(x_val)

        # Metrics
        rmse = mean_squared_error(y_val, preds)
        r2 = r2_score(y_val, preds)

        # Cross-validation
        kf = KFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
        cv_scores = cross_val_score(
            model, x, y,
            cv=kf,
            scoring="neg_root_mean_squared_error"
        )
        cv_rmse = np.mean(-cv_scores)

        # Print model results:
        print(f"Validation RMSE: {rmse}")
        print(f"Validation R2: {r2}")
        print(f"CV RMSE: {cv_rmse}")

        # Log model and parameters in MLFlow:
        mlflow.sklearn.log_model(model, "model")
        mlflow.log_param("model_type", MODEL_CONFIG["model_type"])
        for param_name, param_value in MODEL_CONFIG["params"].items():
            mlflow.log_param(param_name, param_value)

        # Log performance metrics in MLFlow:
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("cv_rmse", cv_rmse)
        mlflow.log_metric("r2", r2)

        # Save model Locally:
        os.makedirs("model", exist_ok=True)
        joblib.dump(model, MODEL_PATH)


# Entry point:
if __name__ == "__main__":
    train(TRAIN_DATA_PATH)