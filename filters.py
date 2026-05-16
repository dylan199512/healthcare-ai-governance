import streamlit as st
import pandas as pd
from governance_utils.governance_logic import calculate_scores

df = pd.read_csv("data/models.csv")
df["governance_score"] = df.apply(calculate_scores, axis=1)

st.title("Interactive Governance Filters")

risk_filter = st.multiselect("Risk Level", ["yes", "no"])
bias_filter = st.multiselect("Bias Level", ["low", "medium", "high"])
score_range = st.slider("Governance Score Range", 0, 100, (0, 100))

filtered = df.copy()

if risk_filter:
    filtered = filtered[filtered["high_risk"].isin(risk_filter)]

if bias_filter:
    filtered = filtered[filtered["bias_level"].isin(bias_filter)]

filtered = filtered[
    (filtered["governance_score"] >= score_range[0]) &
    (filtered["governance_score"] <= score_range[1])
]

st.dataframe(filtered)
