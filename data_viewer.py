import streamlit as st
import pandas as pd

def run(df: pd.DataFrame):
    st.title("Data Viewer")

    st.write("Raw model governance dataset with computed scores and risk tiers.")
    st.dataframe(df)
