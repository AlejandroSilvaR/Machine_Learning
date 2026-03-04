"""
    Data loading utilities.

    This module isolates all data access logic.
    If data source changes (database, S3, etc.), only this file needs modification.
"""

import pandas as pd

def load_training_data(path: str):
    """
        Load training dataset.

        Parameters
        ----------
        path : str
            Path to training CSV file.

        Returns
        -------
        x : pd.DataFrame
            Feature matrix.
        y : pd.Series
            Target variable.
    """

    df = pd.read_csv(path)
    x = df.drop(columns=["target"])
    y = df["target"]
    return x, y

def load_blind_data(path: str):
    """
        Load blind test dataset.

        Parameters
        ----------
        path : str
            Path to blind test CSV file.

        Returns
        -------
        pd.DataFrame
            Feature matrix.
    """
    
    return pd.read_csv(path)