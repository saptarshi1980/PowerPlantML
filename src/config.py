from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
STREAMLIT_DIR = PROJECT_ROOT / "streamlit"

TARGET = "Nett Load (MW)"
RANDOM_STATE = 42
TEST_SIZE = 0.2

MODEL_FILE = MODEL_DIR / "best_model.pkl"
FEATURE_FILE = MODEL_DIR / "feature_columns.pkl"
METRICS_FILE = MODEL_DIR / "metrics.json"
MODEL_INFO_FILE = MODEL_DIR / "model_info.json"