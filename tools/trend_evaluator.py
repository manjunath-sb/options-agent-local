from data.loader import load_company_snapshot

def evaluate_trend_strength():
    snapshot = load_company_snapshot()
    trend = snapshot["trend"]
    volume_trend = snapshot["volume_trend"]
    market_bias = snapshot["market_bias"]

    if trend in ["bullish", "bearish"]:
        direction = trend
    else:
        direction = "sideways"

    score = 0

    if direction == volume_trend:
        score += 1
    elif volume_trend in ["increasing", "decreasing"]:
        score -= 1

    if direction == market_bias:
        score += 1
    elif market_bias in ["bullish", "bearish"]:
        score -= 1


    if score >= 2:
        confidence = "high"
    elif score == 1:
        confidence = "medium"
    else:
        confidence = "low"

    return {
        "direction": direction,
        "confidence": confidence
    }
