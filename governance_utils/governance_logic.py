import pandas as pd

def calculate_scores(row: pd.Series) -> int:
    """
    Multi-factor governance scoring aligned with models.csv columns.
    """
    score = 0

    # 1. Data diversity
    score += 20 if str(row["data_diverse"]).lower() == "yes" else 0

    # 2. Human oversight
    score += 20 if str(row["human_oversight"]).lower() == "yes" else 0

    # 3. Explainability
    score += 20 if str(row["explainable"]).lower() == "yes" else 0

    # 4. High-risk task penalty
    score += -15 if str(row["high_risk_task"]).lower() == "yes" else 10

    # 5. Bias level mapping
    bias_map = {
        "low": 20,
        "medium": 10,
        "high": -20
    }
    bias_flag = str(row["bias_flag"]).lower()
    score += bias_map.get(bias_flag, 0)

    # Final normalization
    return max(0, min(100, score))
