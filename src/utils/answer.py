from src.pipelines.epa_state_msw import get_recycling_rate


def format_summary(question: str, route: dict) -> str:
    intent = route.get("intent", "waste_overview")
    time_range = route.get("time_range", "2015-2024")
    state = route.get("state")
    dataset = route.get("dataset", "epa_state_msw")
    
    # Try to get real data for recycling_rate queries
    if intent == "recycling_rate" and state and time_range:
        metric = get_recycling_rate(state, time_range)
        if metric:
            return (
                f"Recycling rate for {state} in {time_range}: "
                f"{metric['value']}% (EPA State MSW dataset)."
            )
    
    # Fallback to routing summary
    if state:
        location_text = f"{state} in {time_range}"
    else:
        location_text = f"{time_range}"
    return (
        f"Intent: {intent}. "
        f"Target: {location_text}. "
        f"Dataset: {dataset}."
    )

