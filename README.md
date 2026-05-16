# AI Governance Dashboard
A modular evaluation platform for analyzing governance quality in healthcare AI systems. The dashboard supports model scoring, risk visualization, narrative reporting, and PDF export. Organizations can use the tool to review fairness, oversight, explainability, and operational risk across multiple models.

# Key Features
- Governance Scoring: A structured scoring engine that produces a 0 to 100 governance score for each model.

- Interactive Dashboard: A Streamlit interface for exploring models, filtering attributes, and reviewing governance indicators.

- Narrative Reports: Automatically generated summaries that highlight strengths, weaknesses, and recommended actions.

- PDF Export: A report generator that produces clean, readable PDF governance assessments.

- Visual Analytics: Heatmaps, score breakdowns, and risk distribution charts.

- Modular Codebase: A clear separation of concerns across utilities, dashboards, and scoring logic.

# Project Structure**
healthcare-ai-governance/
│
├── launcher.py
├── data/
├── governance_utils/
│   ├── data_loader.py
│   ├── calculate_scores.py
│   ├── governance_logic.py
│   ├── report_generator.py
│   └── __init__.py
│
├── model_dashboard.py
├── risk_dashboard.py
├── summary.py
├── ui.py
├── visualizations.py
├── filters.py
├── requirements.txt
└── README.md


# Governance Scoring Framework
A model receives a governance score based on several criteria:

- Bias risk
- Data diversity
- Explainability
- Human oversight
- High risk task flags
- Domain context


Each criterion contributes to a final numeric score. The score feeds into narrative reporting and PDF generation.

# Visual Analytics
The dashboard includes:

- Bias heatmaps
- Score breakdown charts
- Risk distribution views
- Model comparison panels

# PDF Reporting
Each model can produce a governance report that includes:

- Narrative assessment
- Strengths
- Weaknesses
- Recommendations

# Technology Stack
- Python
- Streamlit
- Pandas
- ReportLab
- Matplotlib
- Seaborn

