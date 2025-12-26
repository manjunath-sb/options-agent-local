from data.loader import load_company_snapshot

def evaluate_volatility_regime():
        snapshot = load_company_snapshot()

        volatility_level = snapshot["volatility_level"]
        iv_percentile = int(snapshot["iv_percentile"])

        if iv_percentile >= 70:
            option_pricing = "expensive"
        elif iv_percentile >= 40:
            option_pricing = "fair"
        else:
            option_pricing = "cheap"

        return {
            "volatility_regime": volatility_level,
            "option_pricing": option_pricing
        }


