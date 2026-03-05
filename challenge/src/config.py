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
    "params": {'loss': 'squared_error',
               'learning_rate': 0.1,
               'n_estimators': 300,
               'subsample': 0.8,
               'criterion': 'friedman_mse',
               'min_samples_split': 2,
               'min_samples_leaf': 5,
               'min_weight_fraction_leaf': 0.0,
               'max_depth': 2,
               'min_impurity_decrease': 0.0,
               'init': None,
               'max_features': None,
               'alpha': 0.9,
               'verbose': 0,
               'max_leaf_nodes': None,
               'warm_start': False,
               'validation_fraction': 0.1,
               'n_iter_no_change': None,
               'tol': 0.0001,
               'ccp_alpha': 0.0}
}

# -----------------------------
# Paths
# -----------------------------
TRAIN_DATA_PATH = BASE_DIR / "data" / "training_data.csv"
TEST_DATA_PATH = BASE_DIR / "data" / "blind_test_data.csv"
RESULTS_DATA_PATH_DEMO_NOTEBOOK = BASE_DIR / "data" / "predictions_method_4.csv"
MODEL_PATH = BASE_DIR / "model" / "model.pkl"