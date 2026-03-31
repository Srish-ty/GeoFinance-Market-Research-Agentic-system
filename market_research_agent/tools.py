from typing import Dict, List


def get_global_news(topic: str) -> Dict:
    """
    Mock tool for phase-1 demo.
    Later you can replace this with a real news API call.
    """
    topic_lower = topic.lower()

    demo_news = {
        "oil": [
            "Crude oil prices remain volatile amid geopolitical tensions in the Middle East.",
            "Shipping and energy supply concerns are influencing global commodity markets.",
            "Aviation and logistics sectors may face pressure if fuel prices stay elevated."
        ],
        "war": [
            "Geopolitical conflict has increased uncertainty across global equity markets.",
            "Energy and defense sectors are seeing increased attention from investors.",
            "Risk-off sentiment may impact emerging markets in the short term."
        ],
        "inflation": [
            "Sticky inflation is increasing expectations of prolonged higher interest rates.",
            "Banking and consumer sectors may respond differently based on policy outlook.",
            "Rate-sensitive sectors may remain under pressure."
        ],
        "interest rates": [
            "Central bank commentary suggests cautious policy decisions ahead.",
            "Higher rates can affect borrowing-heavy sectors and growth stocks.",
            "Financial services may benefit from some rate environments."
        ],
    }

    matched_key = None
    for key in demo_news:
        if key in topic_lower:
            matched_key = key
            break

    if matched_key:
        return {
            "topic": topic,
            "headlines": demo_news[matched_key],
            "source_type": "mock_demo_data"
        }

    return {
        "topic": topic,
        "headlines": [
            f"Recent developments related to '{topic}' are being monitored.",
            "Market participants are evaluating possible sector-level implications.",
            "Further quantitative validation is needed before drawing conclusions."
        ],
        "source_type": "mock_demo_data"
    }


def analyze_macro_impact(topic: str) -> Dict:
    """
    Simple deterministic macro impact mapping tool.
    """
    t = topic.lower()

    if "oil" in t or "crude" in t or "middle east" in t:
        return {
            "event": topic,
            "sentiment": "mixed_to_risk_off",
            "affected_sectors_positive": ["Energy", "Oil & Gas", "Defense"],
            "affected_sectors_negative": ["Aviation", "Logistics", "Paints", "Consumer"],
            "time_horizon": "short_to_medium_term",
            "reasoning": "Higher oil prices can benefit producers, while fuel-sensitive industries may face cost pressure."
        }

    if "war" in t or "conflict" in t or "sanction" in t:
        return {
            "event": topic,
            "sentiment": "risk_off",
            "affected_sectors_positive": ["Defense", "Energy"],
            "affected_sectors_negative": ["Travel", "Consumer", "Import-dependent sectors"],
            "time_horizon": "short_term",
            "reasoning": "Conflict and sanctions can increase uncertainty, disrupt supply chains, and create volatility."
        }

    if "inflation" in t:
        return {
            "event": topic,
            "sentiment": "cautious",
            "affected_sectors_positive": ["FMCG (selective)", "Banks (selective)"],
            "affected_sectors_negative": ["Rate-sensitive sectors", "Consumer discretionary"],
            "time_horizon": "medium_term",
            "reasoning": "Persistent inflation can reduce spending power and influence policy rates."
        }

    if "interest" in t or "fed" in t or "rate" in t:
        return {
            "event": topic,
            "sentiment": "policy_sensitive",
            "affected_sectors_positive": ["Banks", "Financial Services"],
            "affected_sectors_negative": ["High-growth tech", "Real estate", "Borrowing-heavy businesses"],
            "time_horizon": "short_to_medium_term",
            "reasoning": "Rate changes influence capital costs, lending spreads, and equity valuations."
        }

    return {
        "event": topic,
        "sentiment": "neutral_to_cautious",
        "affected_sectors_positive": ["Sector impact needs further evaluation"],
        "affected_sectors_negative": ["Sector impact needs further evaluation"],
        "time_horizon": "uncertain",
        "reasoning": "No specific mapping rule matched. More detailed market research is required."
    }


def get_market_snapshot(symbol: str) -> Dict:
    """
    Mock market data tool for phase-1 demo.
    Replace later with yfinance / real market API if needed.
    """
    sample_data = {
        "RELIANCE": {
            "symbol": "RELIANCE",
            "price": 2985.40,
            "day_high": 3012.00,
            "day_low": 2968.10,
            "trend": "slightly_bullish",
            "notes": "Large-cap energy and diversified business exposure."
        },
        "ONGC": {
            "symbol": "ONGC",
            "price": 284.15,
            "day_high": 289.00,
            "day_low": 281.35,
            "trend": "bullish",
            "notes": "Sensitive to crude and energy market dynamics."
        },
        "IOC": {
            "symbol": "IOC",
            "price": 174.80,
            "day_high": 176.20,
            "day_low": 172.95,
            "trend": "neutral",
            "notes": "Oil marketing exposure; margins can be policy and crude sensitive."
        },
        "INDIGO": {
            "symbol": "INDIGO",
            "price": 4321.90,
            "day_high": 4378.00,
            "day_low": 4290.00,
            "trend": "cautious",
            "notes": "Fuel prices are a key variable for airlines."
        },
        "HDFCBANK": {
            "symbol": "HDFCBANK",
            "price": 1689.30,
            "day_high": 1701.00,
            "day_low": 1675.10,
            "trend": "steady",
            "notes": "Large private banking exposure; rate cycle matters."
        },
    }

    symbol_upper = symbol.upper().strip()
    if symbol_upper in sample_data:
        return sample_data[symbol_upper]

    return {
        "symbol": symbol_upper,
        "price": None,
        "day_high": None,
        "day_low": None,
        "trend": "unknown",
        "notes": "No demo data available for this symbol yet."
    }