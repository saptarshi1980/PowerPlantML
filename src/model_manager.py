"""
Model Manager

Responsible for loading trained ML artifacts.
"""

import joblib


class ModelManager:

    def __init__(self, model_path, feature_path):

        self.model = joblib.load(model_path)

        self.features = joblib.load(feature_path)

    def get_model(self):

        return self.model

    def get_features(self):

        return self.features