import streamlit as st
import pandas as pd
import altair as alt

def run(df: pd.DataFrame):
    st.title("Governance Score Overview")

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("model_name:N", sort="-y", title="Model"),
        y=alt.Y("governance_score:Q", title="Governance Score"),
        color="governance_score:Q",
        tooltip=["model_name", "governance_score", "risk_tier", "domain"]
    ).properties(height=400)

    st.altair_chart(chart, use_container_width=True)
