import streamlit as st
from governance_utils.data_loader import load_data

st.title("CSV Test — Load & Score")

df = load_data()

st.write("Rows loaded:", len(df))
st.write("Columns:", list(df.columns))
st.dataframe(df)
