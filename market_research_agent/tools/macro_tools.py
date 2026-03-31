def get_global_news(topic: str) -> dict:
    return {
        "topic": topic,
        "headlines": [
            f"Recent developments related to {topic} are affecting investor sentiment.",
            "Global macro conditions are influencing sector-level movements."
        ]
    }


def analyze_macro_impact(topic: str) -> dict:
    topic = topic.lower()

    if "oil" in topic or "crude" in topic:
        return {
            "sentiment": "mixed",
            "positive_sectors": ["Energy", "Oil & Gas"],
            "negative_sectors": ["Aviation", "Logistics"],
            "reason": "Higher fuel costs may pressure fuel-sensitive sectors while supporting producers."
        }

    if "inflation" in topic:
        return {
            "sentiment": "cautious",
            "positive_sectors": ["Banks"],
            "negative_sectors": ["Consumer Discretionary"],
            "reason": "Persistent inflation may affect demand and policy rates."
        }

    return {
        "sentiment": "neutral",
        "positive_sectors": [],
        "negative_sectors": [],
        "reason": "No strong sector mapping found."
    }