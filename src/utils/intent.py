def infer_intent(question: str) -> str:
    question_lower = question.lower()
    if "recycle" in question_lower or "recycling" in question_lower:
        return "recycling_rate"
    if "landfill" in question_lower:
        return "landfill_share"
    if "organic" in question_lower or "compost" in question_lower:
        return "organic_diversion"
    if "plastic" in question_lower:
        return "plastic_stream"
    return "waste_overview"

