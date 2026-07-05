import streamlit as st
import pandas as pd
from pathlib import Path
import sys

# -------------------------------------------------------
# Project Path
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.append(str(PROJECT_ROOT))

from src.predict import PowerPlantPredictor

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title="Single Prediction",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 Single Prediction")

st.markdown(
"""
Predict the **Net Load (MW)** using the trained XGBoost model.

The page automatically loads a sample operating condition from the dataset.
Simply modify any values you wish and click **Predict**.
"""
)

# -------------------------------------------------------
# Load Predictor
# -------------------------------------------------------

predictor = PowerPlantPredictor()

# -------------------------------------------------------
# Load Sample Dataset
# -------------------------------------------------------

DATA_FILE = PROJECT_ROOT / "data" / "industrial_dataset.csv"

try:

    sample_df = pd.read_csv(DATA_FILE)

    if "Timestamp" in sample_df.columns:
        sample_df = sample_df.drop(columns=["Timestamp"])

    st.sidebar.success("Sample dataset loaded.")

except Exception as e:

    st.error(f"Cannot load dataset.\n\n{e}")
    st.stop()

# -------------------------------------------------------
# Select Sample Row
# -------------------------------------------------------

sample_index = st.sidebar.number_input(
    "Sample Row",
    min_value=0,
    max_value=len(sample_df) - 1,
    value=0,
    step=1
)

default_values = sample_df.iloc[sample_index].to_dict()

st.sidebar.write(f"Using sample #{sample_index}")

# -------------------------------------------------------
# Categorize Features
# -------------------------------------------------------

groups = {
    "🔥 Boiler Parameters": [],
    "⚙️ Turbine Parameters": [],
    "💧 Feedwater Parameters": [],
    "🌫️ Emission Parameters": [],
    "📈 Performance Parameters": [],
    "📦 Other Parameters": []
}

for feature in predictor.feature_columns:

    f = feature.lower()

    if "boiler" in f or "steam" in f or "coal" in f:
        groups["🔥 Boiler Parameters"].append(feature)

    elif "turbine" in f or "reheat" in f:
        groups["⚙️ Turbine Parameters"].append(feature)

    elif "feedwater" in f:
        groups["💧 Feedwater Parameters"].append(feature)

    elif (
        "so2" in f
        or "nox" in f
        or "co2" in f
        or "co (" in f
        or "dust" in f
        or "opacity" in f
        or "oxygen" in f
        or "o2" in f
    ):
        groups["🌫️ Emission Parameters"].append(feature)

    elif (
        "eff" in f
        or "load" in f
        or "vacuum" in f
        or "enthalpy" in f
        or "entropy" in f
    ):
        groups["📈 Performance Parameters"].append(feature)

    else:
        groups["📦 Other Parameters"].append(feature)

# -------------------------------------------------------
# Input Form
# -------------------------------------------------------

values = {}

with st.form("prediction_form"):

    for group_name, features in groups.items():

        if len(features) == 0:
            continue

        with st.expander(group_name, expanded=False):

            col1, col2 = st.columns(2)

            for i, feature in enumerate(features):

                value = float(default_values.get(feature, 0))

                if i % 2 == 0:
                    with col1:
                        values[feature] = st.number_input(
                            feature,
                            value=value,
                            format="%.6f"
                        )
                else:
                    with col2:
                        values[feature] = st.number_input(
                            feature,
                            value=value,
                            format="%.6f"
                        )

    submitted = st.form_submit_button(
        "🚀 Predict Net Load"
    )

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

if submitted:

    input_df = pd.DataFrame([values])

    prediction = predictor.predict(input_df)[0]

    st.markdown("---")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.success("Prediction completed successfully.")

        st.metric(
            label="Predicted Net Load",
            value=f"{prediction:.3f} MW"
        )

        st.info(
            """
The prediction is generated using the trained
**Optimized XGBoost** model.
"""
        )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.markdown("---")

st.caption(
    "Industrial Power Plant AI • Single Prediction Module"
)