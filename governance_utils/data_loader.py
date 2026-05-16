import pandas as pd
from governance_utils.governance_logic import calculate_scores

def assign_risk_tier(score: int) -> str:
    if score < 50:
        return "🔴 High governance risk"
    elif score < 75:
        return "🟡 Moderate governance risk"
    else:
        return "🟢 Low governance risk"

def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/models.csv")
    df["governance_score"] = df.apply(calculate_scores, axis=1)
    df["risk_tier"] = df["governance_score"].apply(assign_risk_tier)
    return df
