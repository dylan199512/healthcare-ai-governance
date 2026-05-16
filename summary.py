import streamlit as st
import pandas as pd

def run(df: pd.DataFrame):
    st.title("Summary Report")

    st.subheader("Overall Governance Snapshot")

    col1, col2, col3 = st.columns(3)
    col1.metric("Models", len(df))
    col2.metric("Avg Governance Score", round(df["governance_score"].mean(), 1))
    col3.metric("High-Risk Models", int((df["risk_tier"] == "🔴 High governance risk").sum()))

    st.subheader("Risk Tier Distribution")
    st.bar_chart(df["risk_tier"].value_counts())

    st.subheader("Average Governance Score by Domain")
    domain_scores = df.groupby("domain")["governance_score"].mean().sort_values(ascending=False)
    st.bar_chart(domain_scores)
