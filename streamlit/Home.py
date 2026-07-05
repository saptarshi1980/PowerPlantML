"""
Industrial Power Plant AI
Home Page
"""

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
# Header
# -------------------------------------------------------

st.title("🏭 Industrial Power Plant AI")

st.subheader(
    "AI Decision Support System for Thermal Power Plants"
)

st.markdown("---")

# -------------------------------------------------------
# Introduction
# -------------------------------------------------------

st.markdown(
"""
Modern thermal power plants generate enormous volumes of operating
data every minute.

This application uses **Artificial Intelligence** to estimate
the expected **Net Power Generation (MW)** from current plant
operating conditions.

Rather than replacing plant engineers, the objective is to
provide **decision support** by transforming operational data
into actionable insights.
"""
)

st.markdown("---")

# -------------------------------------------------------
# Key Capabilities
# -------------------------------------------------------

st.header("🚀 Key Capabilities")

col1, col2 = st.columns(2)

with col1:

    st.success(
"""
### 🔮 Single Prediction

Predict the expected Net Load (MW)
for a single operating condition.
"""
    )

    st.success(
"""
### 📂 Batch Prediction

Upload historical operating data
and predict Net Load for thousands
of records.
"""
    )

with col2:

    st.success(
"""
### 🧠 AI Insights

Understand which operating
parameters have the greatest
influence on plant generation.
"""
    )

    st.success(
"""
### 📈 Plant Analytics

Explore historical operating
patterns and relationships
between important plant variables.
"""
    )

st.markdown("---")

# -------------------------------------------------------
# Workflow
# -------------------------------------------------------

st.header("⚙ AI Decision Support Workflow")

st.info("""
Plant Operating Data

⬇

AI Prediction Engine

⬇

Predicted Net Load

⬇

AI Insights

⬇

Better Operational Decisions
""")

st.markdown("---")

# -------------------------------------------------------
# Business Value
# -------------------------------------------------------

st.header("💡 Business Value")

left, right = st.columns(2)

with left:

    st.markdown("""
### Benefits to Plant Engineers

- Estimate expected generation.

- Evaluate operating scenarios.

- Understand important plant parameters.

- Analyse historical operating data.

- Support operational decision making.
""")

with right:

    st.markdown("""
### Benefits to Management

- Encourage data-driven decisions.

- Improve operational awareness.

- Demonstrate AI adoption.

- Reduce manual analysis effort.

- Support digital transformation.
""")

st.markdown("---")

# -------------------------------------------------------
# Future Vision
# -------------------------------------------------------

st.header("🚀 Future Roadmap")

st.write("""
The current version demonstrates AI-based
prediction of Net Load.

Future versions may include:

- Real-time SCADA integration

- Equipment health monitoring

- Boiler efficiency optimisation

- Turbine performance monitoring

- Early fault detection

- AI-powered operational recommendations
""")

st.markdown("---")

st.success(
"Industrial Power Plant AI is designed as an AI-assisted decision support platform—not an autonomous control system."
)

st.caption(
"Developed using Python • XGBoost • Optuna • SHAP • Streamlit"
)