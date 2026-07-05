"""
Data Loading Module
"""

from pathlib import Path
import pandas as pd


def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"{file_path} not found."
        )

    return pd.read_csv(file_path)


def save_csv(df, file_path):
    """
    Save DataFrame to CSV.
    """
    file_path = Path(file_path)

    df.to_csv(
        file_path,
        index=False
    )