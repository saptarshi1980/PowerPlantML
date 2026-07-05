from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_ROOT / "models"

DATA_DIR = PROJECT_ROOT / "data"

TARGET = "Nett Load (MW)"

MODEL_FILE = MODEL_DIR / "best_model.pkl"

FEATURE_FILE = MODEL_DIR / "feature_columns.pkl"

MODEL_INFO = MODEL_DIR / "model_info.json"