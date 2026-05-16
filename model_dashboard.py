import streamlit as st
import pandas as pd
from governance_utils.report_generator import generate_governance_report

def run(df: pd.DataFrame):
    st.title("Model Governance Dashboard")

    model_name = st.selectbox("Select Model", df["model_name"].tolist())
    row = df[df["model_name"] == model_name].iloc[0]

    score = row["governance_score"]
    risk_tier = row["risk_tier"]
    report = generate_governance_report(row, score)

    col1, col2 = st.columns(2)
    col1.metric("Governance Score", score)
    col2.metric("Risk Tier", risk_tier)

    st.subheader("Model Metadata")
    st.write(f"**Description:** {row.get('description', '')}")
    st.write(f"**Domain:** {row.get('domain', '')}")
    st.write(f"**Synthetic Risk Score:** {row.get('synthetic_risk_score', '')}")

    st.subheader("Narrative Summary")
    st.write(report["narrative"])

    with st.expander("Strengths"):
        for s in report["strengths"]:
            st.write(f"- {s}")

    with st.expander("Weaknesses"):
        for w in report["weaknesses"]:
            st.write(f"- {w}")

    with st.expander("Recommendations"):
        for r in report["recommendations"]:
            st.write(f"- {r}")
