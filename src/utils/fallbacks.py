def fallback_response() -> dict:
    return {
        "intent": "waste_overview",
        "dataset": "waste_streams",
        "granularity": "city",
        "time_range": "2015-2024",
        "note": "Fallback route applied.",
    }

