def calculate_scores(row):
    """
    Multi-factor governance scoring aligned with the CSV column names.
    """

    score = 0

    # 1. Data diversity
    score += 20 if row["data_diverse"] == "yes" else 0

    # 2. Human oversight
    score += 20 if row["human_oversight"] == "yes" else 0

    # 3. Explainability (CSV uses 'explainable')
    score += 20 if row["explainable"] == "yes" else 0

    # 4. High-risk task penalty (CSV uses 'high_risk_task')
    score += -15 if row["high_risk_task"] == "yes" else 10

    # 5. Bias level mapping (CSV uses 'bias_flag')
    bias_map = {
        "low": 20,
        "medium": 10,
        "high": -20
    }
    score += bias_map.get(row["bias_flag"].lower(), 0)

    # Final normalization
    return max(0, min(100, score))
