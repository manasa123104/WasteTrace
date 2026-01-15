import re

from src.utils.intent import infer_intent

STATES = [
    "alabama",
    "alaska",
    "arizona",
    "arkansas",
    "california",
    "colorado",
    "connecticut",
    "delaware",
    "florida",
    "georgia",
    "hawaii",
    "idaho",
    "illinois",
    "indiana",
    "iowa",
    "kansas",
    "kentucky",
    "louisiana",
    "maine",
    "maryland",
    "massachusetts",
    "michigan",
    "minnesota",
    "mississippi",
    "missouri",
    "montana",
    "nebraska",
    "nevada",
    "new hampshire",
    "new jersey",
    "new mexico",
    "new york",
    "north carolina",
    "north dakota",
    "ohio",
    "oklahoma",
    "oregon",
    "pennsylvania",
    "rhode island",
    "south carolina",
    "south dakota",
    "tennessee",
    "texas",
    "utah",
    "vermont",
    "virginia",
    "washington",
    "west virginia",
    "wisconsin",
    "wyoming",
]


def _extract_state(question: str) -> str | None:
    question_lower = question.lower()
    for state in STATES:
        if state in question_lower:
            return state.title()
    return None


def route_query(question: str) -> dict:
    intent = infer_intent(question)
    state = _extract_state(question)
    year_matches = re.findall(r"\b(20\d{2})\b", question)
    if year_matches:
        time_range = year_matches[0]
    else:
        time_range = "2015-2024"
    return {
        "intent": intent,
        "dataset": "epa_state_msw",
        "granularity": "state",
        "state": state,
        "time_range": time_range,
    }

