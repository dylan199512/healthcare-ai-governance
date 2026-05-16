import streamlit as st
import pandas as pd
from governance_utils.report_generator import generate_governance_report, export_report_to_pdf

def run(df: pd.DataFrame):
    st.title("Governance Scoring & Report Generator")

    model_name = st.selectbox("Model Name", df["model_name"].tolist())
    row = df[df["model_name"] == model_name].iloc[0]

    score = row["governance_score"]
    report = generate_governance_report(row, score)

    st.success(f"Governance Score for {model_name}: {score}")

    st.subheader("Narrative Summary")
    st.write(report["narrative"])

    st.subheader("Strengths")
    for s in report["strengths"]:
        st.write(f"- {s}")

    st.subheader("Weaknesses")
    for w in report["weaknesses"]:
        st.write(f"- {w}")

    st.subheader("Recommendations")
    for r in report["recommendations"]:
        st.write(f"- {r}")

    pdf_bytes = export_report_to_pdf(report)
    st.download_button(
        label="Download Governance Report (PDF)",
        data=pdf_bytes,
        file_name=f"{model_name}_governance_report.pdf",
        mime="application/pdf",
    )
