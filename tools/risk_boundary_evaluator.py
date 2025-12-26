from data.loader import load_company_snapshot

def evaluate_risk_boundaries():
    snapshot = load_company_snapshot()
        
    support_near = snapshot["support_near"]
    resistance_near = snapshot["resistance_near"]

    downside_risk_defined = support_near == "yes"
    upside_risk_capped = resistance_near == "yes"

    if downside_risk_defined and upside_risk_capped:
        risk_clarity = "high"
    elif downside_risk_defined or upside_risk_capped:
        risk_clarity = "medium"
    else:
        risk_clarity = "low"

    return {
        "downside_risk_defined": downside_risk_defined,
        "upside_risk_capped": upside_risk_capped,
        "risk_clarity": risk_clarity
    }



