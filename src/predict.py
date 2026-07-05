"""
Prediction Module
"""

from pathlib import Path

import pandas as pd

from src.config import FEATURE_FILE, MODEL_FILE
from src.model_manager import ModelManager


class PowerPlantPredictor:
    """
    Backend prediction engine for the Power Plant AI application.
    """

    def __init__(self):

        manager = ModelManager(
            MODEL_FILE,
            FEATURE_FILE
        )

        self.model = manager.get_model()
        self.feature_columns = manager.get_features()

    @property
    def model_name(self):
        return type(self.model).__name__

    @property
    def num_features(self):
        return len(self.feature_columns)

    def predict(self, input_df):

        if not isinstance(input_df, pd.DataFrame):
            raise TypeError("Input must be a pandas DataFrame.")

        missing = list(
            set(self.feature_columns) -
            set(input_df.columns)
        )

        if missing:
            raise ValueError(
                f"Missing columns: {missing}"
            )

        input_df = input_df[self.feature_columns]

        return self.model.predict(input_df)

    def get_feature_names(self):
        return self.feature_columns