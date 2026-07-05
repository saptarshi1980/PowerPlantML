"""
AI Insights Dashboard
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

from src.ui import page_header, show_footer

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Insights",
    page_icon="🧠",
    layout="wide"
)

page_header(
    "🧠 AI Insights",
    """
Understand which operating parameters have the greatest influence
on the predicted Net Load.
"""
)

# -------------------------------------------------------
# Load Feature Importance
# -------------------------------------------------------

importance_file = PROJECT_ROOT / "models" / "feature_importance.csv"

importance = pd.read_csv(importance_file)

# -------------------------------------------------------
# Top Parameters
# -------------------------------------------------------

st.subheader("Top 20 Influential Parameters")

top20 = importance.head(20)

st.bar_chart(
    top20.set_index("Feature")["Importance"]
)

# -------------------------------------------------------
# Table
# -------------------------------------------------------

st.subheader("Feature Ranking")

st.dataframe(
    top20,
    use_container_width=True,
    hide_index=True
)

# -------------------------------------------------------
# Engineering Interpretation
# -------------------------------------------------------

st.subheader("Engineering Interpretation")

top5 = top20.head(5)

for _, row in top5.iterrows():

    st.success(
        f"**{row['Feature']}** is one of the most influential "
        f"parameters affecting the predicted Net Load."
    )

# -------------------------------------------------------
# AI Summary
# -------------------------------------------------------

st.subheader("AI Summary")

highest = importance.iloc[0]["Feature"]

st.info(
    f"""
The trained AI model has learned that **{highest}** has the
greatest impact on Net Load prediction.

Changes in this parameter have a stronger influence on the
predicted generation than most other operating variables.

Engineers should therefore pay particular attention to this
parameter during load changes and performance monitoring.
"""
)

show_footer()