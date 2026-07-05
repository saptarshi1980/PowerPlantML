"""
Model Manager

Responsible for loading trained ML artifacts.
"""

from pathlib import Path
import joblib


class ModelManager:
    """
    Loads and provides access to trained model artifacts.
    """

    def __init__(self, model_path: Path, feature_path: Path):

        self._model = joblib.load(model_path)
        self._feature_columns = joblib.load(feature_path)

    def get_model(self):
        """Return the trained model."""
        return self._model

    def get_features(self):
        """Return the ordered feature list."""
        return self._feature_columns

    def get_model_name(self):
        """Return the model class name."""
        return type(self._model).__name__

    def get_feature_count(self):
        """Return number of input features."""
        return len(self._feature_columns)