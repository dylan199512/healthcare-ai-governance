import streamlit as st
from governance_utils.data_loader import load_data
import summary
import scoring
import data_viewer
import model_dashboard
import risk_dashboard
import visualizations

def main():
    st.set_page_config(page_title="AI Governance Dashboard", layout="wide")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        [
            "📊 Summary Report",
            "🧮 Governance Scoring",
            "📁 Data Viewer",
            "🧾 Model Governance Dashboard",
            "🚦 Risk Tier Dashboard",
            "📈 Score Visualizations",
        ],
    )

    df = load_data()

    if page == "📊 Summary Report":
        summary.run(df)
    elif page == "🧮 Governance Scoring":
        scoring.run(df)
    elif page == "📁 Data Viewer":
        data_viewer.run(df)
    elif page == "🧾 Model Governance Dashboard":
        model_dashboard.run(df)
    elif page == "🚦 Risk Tier Dashboard":
        risk_dashboard.run(df)
    elif page == "📈 Score Visualizations":
        visualizations.run(df)

if __name__ == "__main__":
    main()
