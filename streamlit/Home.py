import json
from pathlib import Path

import streamlit as st

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Industrial Power Plant AI",
    page_icon="🏭",
    layout="wide"
)

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_ROOT / "models"

METRICS_FILE = MODEL_DIR / "metrics.json"
MODEL_INFO_FILE = MODEL_DIR / "model_info.json"

# -------------------------------------------------------
# Load JSON Files
# -------------------------------------------------------

with open(METRICS_FILE, "r") as f:
    metrics = json.load(f)

with open(MODEL_INFO_FILE, "r") as f:
    info = json.load(f)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

st.sidebar.title("🏭 Industrial Power Plant AI")

st.sidebar.markdown("---")

st.sidebar.write(f"**Version:** {info['version']}")
st.sidebar.write(f"**Algorithm:** {info['algorithm']}")
st.sidebar.write(f"**Platform:** {info['training_platform']}")

st.sidebar.markdown("---")

st.sidebar.success("Backend Loaded Successfully")

# -------------------------------------------------------
# Title
# -------------------------------------------------------

st.title("🏭 Industrial Power Plant AI Dashboard")

st.caption(
    "Predicting Net Power Generation using Machine Learning"
)

st.markdown("---")

# -------------------------------------------------------
# Metrics
# -------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Model",
        info["algorithm"]
    )

with col2:
    st.metric(
        "R² Score",
        f"{metrics['R2']:.3f}"
    )

with col3:
    st.metric(
        "RMSE",
        f"{metrics['RMSE']:.3f}"
    )

with col4:
    st.metric(
        "MAE",
        f"{metrics['MAE']:.3f}"
    )

st.markdown("---")

# -------------------------------------------------------
# Project Information
# -------------------------------------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("📘 Project Overview")

    st.write(
        """
This application predicts the **Net Load (MW)** of an industrial
thermal power plant using an **Optimized XGBoost** regression model.

The model was trained using historical operational data collected
from boiler, turbine and auxiliary plant sensors.
"""
    )

    st.write("### Features")

    st.markdown("""
- ✅ Optimized XGBoost Model
- ✅ Optuna Hyperparameter Tuning
- ✅ SHAP Explainability
- ✅ Batch Prediction
- ✅ Single Prediction
- ✅ CSV Upload Support
""")

with right:

    st.subheader("ℹ Model Details")

    st.info(f"""
**Algorithm**

{info['algorithm']}

---

**Target**

{info['target']}

---

**Optimization**

{info['optimization']}

---

**Explainability**

{info['explainability']}

---

**Version**

{info['version']}
""")

st.markdown("---")

# -------------------------------------------------------
# Model Performance
# -------------------------------------------------------

st.subheader("📊 Model Performance")

perf1, perf2, perf3, perf4 = st.columns(4)

perf1.metric("R²", f"{metrics['R2']:.4f}")
perf2.metric("RMSE", f"{metrics['RMSE']:.4f}")
perf3.metric("MAE", f"{metrics['MAE']:.4f}")
perf4.metric("MAPE", f"{metrics['MAPE']:.2%}")

st.markdown("---")

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.success("✅ Model and configuration loaded successfully.")

st.caption(
    "Industrial Power Plant AI | Developed using Python, XGBoost, Optuna, SHAP and Streamlit"
)