def get_market_snapshot(symbol: str) -> dict:
    sample = {
        "RELIANCE": {"price": 2985.40, "trend": "slightly bullish"},
        "ONGC": {"price": 284.15, "trend": "bullish"},
        "IOC": {"price": 174.80, "trend": "neutral"},
        "INDIGO": {"price": 4321.90, "trend": "cautious"},
    }
    return {"symbol": symbol, **sample.get(symbol.upper(), {"price": None, "trend": "unknown"})}