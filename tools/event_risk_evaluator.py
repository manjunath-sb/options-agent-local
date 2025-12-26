from data.loader import load_company_snapshot

def evaluate_event_risk():
    snapshot = load_company_snapshot()
    days_to_event = int(snapshot["days_to_event"])

    if days_to_event <= 7:
        event_risk = "high"
        event_window = "imminent"
    elif days_to_event <= 20:
        event_risk = "medium"
        event_window = "near"
    else:
        event_risk = "low"
        event_window = "distant"

    return {
        "event_risk": event_risk,
        "event_window": event_window
    }



