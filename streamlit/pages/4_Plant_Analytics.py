"""
Plant Analytics Dashboard
"""

from pathlib import Path
import sys

import pandas as pd
import plotly.express as px
import streamlit as st

# -------------------------------------------------------
# Project Path
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.config import DATA_DIR
from src.ui import page_header, show_footer

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Plant Analytics",
    page_icon="📈",
    layout="wide"
)

page_header(
    "📈 Plant Analytics",
    "Explore historical operating data from the thermal power plant."
)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

DATA_FILE = DATA_DIR / "industrial_dataset.csv"

try:
    df = pd.read_csv(DATA_FILE)
except Exception as e:
    st.error(f"Unable to load dataset.\n\n{e}")
    st.stop()

# -------------------------------------------------------
# Identify Target Column
# -------------------------------------------------------

possible_targets = [
    "Nett Load (MW)",
    "Net Load (MW)",
    "Net Load",
    "Target"
]

target_column = None

for col in possible_targets:
    if col in df.columns:
        target_column = col
        break

if target_column is None:
    st.error("Target column not found.")
    st.write(df.columns.tolist())
    st.stop()

# -------------------------------------------------------
# Dataset Summary
# -------------------------------------------------------

st.subheader("📋 Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Records", f"{len(df):,}")
c2.metric("Parameters", len(df.columns) - 1)
c3.metric("Average Load", f"{df[target_column].mean():.1f} MW")
c4.metric("Maximum Load", f"{df[target_column].max():.1f} MW")

st.divider()

# -------------------------------------------------------
# Net Load Trend
# -------------------------------------------------------

st.subheader("⚡ Net Load Trend")

fig = px.line(
    df,
    y=target_column,
    title="Net Load Variation"
)

fig.update_layout(
    xaxis_title="Record Number",
    yaxis_title="Net Load (MW)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# Load Distribution
# -------------------------------------------------------

st.subheader("📊 Operating Load Distribution")

fig = px.histogram(
    df,
    x=target_column,
    nbins=30,
    title="Distribution of Net Load"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# Parameter Explorer
# -------------------------------------------------------

st.subheader("🔍 Parameter Explorer")

parameters = [
    col for col in df.columns
    if col != target_column
]

selected = st.selectbox(
    "Select Plant Parameter",
    parameters
)

fig = px.line(
    df,
    y=selected,
    title=selected
)

fig.update_layout(
    xaxis_title="Record Number",
    yaxis_title=selected
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------------------------------------
# Correlation with Net Load
# -------------------------------------------------------

st.subheader("📈 Parameters Most Correlated with Net Load")

corr = (
    df.corr(numeric_only=True)[target_column]
    .drop(target_column)
    .abs()
    .sort_values(ascending=False)
    .head(10)
)

corr_df = corr.reset_index()
corr_df.columns = ["Parameter", "Correlation"]

fig = px.bar(
    corr_df,
    x="Correlation",
    y="Parameter",
    orientation="h",
    title="Top Parameters Correlated with Net Load"
)

fig.update_layout(yaxis={"categoryorder": "total ascending"})

st.plotly_chart(
    fig,
    use_container_width=True
)

st.info(
    """
This dashboard helps engineers explore historical operating data,
identify important plant parameters, and better understand operating
patterns before making operational decisions.

The charts are intended to support analysis and demonstration of how
AI can complement engineering judgement.
"""
)

show_footer()