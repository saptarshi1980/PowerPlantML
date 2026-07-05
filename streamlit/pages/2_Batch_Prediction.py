"""
Batch Prediction Page
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# -------------------------------------------------------
# Project Path
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.predict import PowerPlantPredictor
from src.ui import page_header, show_footer

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

page_header(
    "📂 Batch Prediction",
    """
Upload a CSV file containing thermal power plant operating parameters.

The AI model will predict **Net Load (MW)** for every record.
"""
)

# -------------------------------------------------------
# Load Predictor
# -------------------------------------------------------

try:
    predictor = PowerPlantPredictor()

except Exception as e:

    st.error(f"Unable to load prediction model.\n\n{e}")
    st.stop()

# -------------------------------------------------------
# Upload CSV
# -------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is None:

    st.info("Please upload a CSV file to begin.")

    show_footer()

    st.stop()

# -------------------------------------------------------
# Read CSV
# -------------------------------------------------------

try:

    df = pd.read_csv(uploaded_file)

except Exception as e:

    st.error(f"Unable to read CSV.\n\n{e}")

    st.stop()

# -------------------------------------------------------
# Dataset Preview
# -------------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    df.head(),
    use_container_width=True
)

# -------------------------------------------------------
# Validate Columns
# -------------------------------------------------------

missing_columns = list(
    set(predictor.feature_columns) -
    set(df.columns)
)

if missing_columns:

    st.error(
        "The uploaded file is missing required columns."
    )

    st.write(missing_columns)

    st.stop()

# -------------------------------------------------------
# Predict
# -------------------------------------------------------

with st.spinner("Running AI model..."):

    predictions = predictor.predict(df)

# -------------------------------------------------------
# Result
# -------------------------------------------------------

result_df = df.copy()

result_df["Predicted Net Load (MW)"] = predictions

st.success("Prediction completed successfully.")

# -------------------------------------------------------
# KPI Dashboard
# -------------------------------------------------------

st.subheader("Prediction Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Records",
        len(result_df)
    )

with col2:

    st.metric(
        "Average Load",
        f"{result_df['Predicted Net Load (MW)'].mean():.2f} MW"
    )

with col3:

    st.metric(
        "Maximum Load",
        f"{result_df['Predicted Net Load (MW)'].max():.2f} MW"
    )

with col4:

    st.metric(
        "Minimum Load",
        f"{result_df['Predicted Net Load (MW)'].min():.2f} MW"
    )

# -------------------------------------------------------
# Trend Chart
# -------------------------------------------------------

st.subheader("Prediction Trend")

chart_df = pd.DataFrame(
    {
        "Predicted Net Load (MW)":
        result_df["Predicted Net Load (MW)"]
    }
)

st.line_chart(chart_df)

# -------------------------------------------------------
# Prediction Table
# -------------------------------------------------------

st.subheader("Prediction Results")

st.dataframe(
    result_df,
    use_container_width=True
)

# -------------------------------------------------------
# Download
# -------------------------------------------------------

csv = result_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Prediction CSV",
    data=csv,
    file_name="prediction_output.csv",
    mime="text/csv"
)

show_footer()