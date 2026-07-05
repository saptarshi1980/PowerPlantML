import pandas as pd

from src.predict import PowerPlantPredictor
from src.config import DATA_DIR

predictor = PowerPlantPredictor()

sample = pd.read_csv(DATA_DIR / "sample_input.csv")

prediction = predictor.predict(sample)

print("\nPrediction:")
print(prediction)