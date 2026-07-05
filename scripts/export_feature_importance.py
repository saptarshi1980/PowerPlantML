"""
Export Feature Importance from trained model
"""

import joblib
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_FILE = PROJECT_ROOT / "models" / "best_model.pkl"
FEATURE_FILE = PROJECT_ROOT / "models" / "feature_columns.pkl"

model = joblib.load(MODEL_FILE)
features = joblib.load(FEATURE_FILE)

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

OUTPUT_FILE = PROJECT_ROOT / "models" / "feature_importance.csv"

importance.to_csv(
    OUTPUT_FILE,
    index=False
)

print("Export completed.")
print(importance.head(20))