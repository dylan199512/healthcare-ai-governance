from typing import Dict, List
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_governance_report(row: pd.Series, score: int) -> Dict[str, object]:
    name = row["model_name"]
    domain = row.get("domain", "unknown")
    desc = row.get("description", "")

    narrative = (
        f"{name} is an AI system used in the domain of {domain}. "
        f"It received a governance score of {score} out of 100. "
        f"{desc}"
    )

    strengths: List[str] = []
    weaknesses: List[str] = []
    recommendations: List[str] = []

    if str(row["data_diverse"]).lower() == "yes":
        strengths.append("Uses diverse data sources.")
    else:
        weaknesses.append("Data diversity is limited.")
        recommendations.append("Increase diversity of training and evaluation data.")

    if str(row["human_oversight"]).lower() == "yes":
        strengths.append("Human oversight is present.")
    else:
        weaknesses.append("Lacks robust human oversight.")
        recommendations.append("Introduce human-in-the-loop review.")

    if str(row["explainable"]).lower() == "yes":
        strengths.append("Model outputs are explainable.")
    else:
        weaknesses.append("Explainability is limited.")
        recommendations.append("Invest in explainability tooling.")

    if str(row["high_risk_task"]).lower() == "yes":
        weaknesses.append("Model is used for high-risk clinical tasks.")
        recommendations.append("Strengthen monitoring and fallback procedures.")

    bias_flag = str(row["bias_flag"]).lower()
    if bias_flag == "low":
        strengths.append("Bias risk is low.")
    elif bias_flag == "medium":
        weaknesses.append("Bias risk is medium.")
        recommendations.append("Conduct targeted bias audits.")
    elif bias_flag == "high":
        weaknesses.append("Bias risk is high.")
        recommendations.append("Prioritize bias mitigation before scaling.")

    return {
        "narrative": narrative,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "recommendations": recommendations,
    }

def export_report_to_pdf(report: Dict[str, object]) -> bytes:
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    text = c.beginText(40, 750)
    text.setFont("Helvetica", 12)

    text.textLine("AI Governance Report")
    text.textLine("")

    text.textLine("=== Narrative ===")
    for line in report["narrative"].split("\n"):
        text.textLine(line)

    text.textLine("")
    text.textLine("=== Strengths ===")
    for s in report["strengths"]:
        text.textLine(f"- {s}")

    text.textLine("")
    text.textLine("=== Weaknesses ===")
    for w in report["weaknesses"]:
        text.textLine(f"- {w}")

    text.textLine("")
    text.textLine("=== Recommendations ===")
    for r in report["recommendations"]:
        text.textLine(f"- {r}")

    c.drawText(text)
    c.showPage()
    c.save()

    pdf = buffer.getvalue()
    buffer.close()
    return pdf
