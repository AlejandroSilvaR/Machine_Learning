"""
    Configuration module for the Wizeline ML Challenge project.

    This file centralizes:
    - Global constants
    - Model configuration
    - File paths
    - Experiment tracking configuration

    This allows reproducibility and easier maintainability.
"""

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# Data split configuration
# -----------------------------
TEST_SIZE = 0.2
RANDOM_STATE = 42

# -----------------------------
# MLflow experiment
# -----------------------------
MLFLOW_EXPERIMENT = "wizeline_regression_experiment"

# -----------------------------
# Final Model Configuration
# -----------------------------
MODEL_CONFIG = {
    "model_type": "xgboost",  # options: "xgboost", "lightgbm", "random_forest"
    "params": {
        "n_estimators": 200,
        "max_depth": 6,
        "learning_rate": 0.05,
        "random_state": RANDOM_STATE
    }
}

# -----------------------------
# Paths
# -----------------------------
TRAIN_DATA_PATH = BASE_DIR / "data" / "training_data.csv"
TEST_DATA_PATH = BASE_DIR / "data" / "blind_test_data.csv"
RESULTS_DATA_PATH = BASE_DIR / "data" / "predictions.csv"
MODEL_PATH = BASE_DIR / "model" / "model.pkl"