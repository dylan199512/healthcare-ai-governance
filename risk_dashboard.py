import streamlit as st
import pandas as pd

def run(df: pd.DataFrame):
    st.title("Risk Tier Dashboard")

    st.subheader("Risk Tier Distribution")
    tier_counts = df["risk_tier"].value_counts()
    st.bar_chart(tier_counts)

    st.subheader("Average Governance Score by Domain")
    domain_scores = df.groupby("domain")["governance_score"].mean().sort_values(ascending=False)
    st.bar_chart(domain_scores)

    high = df[df["risk_tier"] == "🔴 High governance risk"]
    medium = df[df["risk_tier"] == "🟡 Moderate governance risk"]
    low = df[df["risk_tier"] == "🟢 Low governance risk"]

    st.header("🔴 High Governance Risk Models")
    st.dataframe(high)

    st.header("🟡 Moderate Governance Risk Models")
    st.dataframe(medium)

    st.header("🟢 Low Governance Risk Models")
    st.dataframe(low)
