"""
EPA State Municipal Solid Waste (MSW) data pipeline.

Provides recycling rates and waste metrics by US state from EPA datasets.
"""

# Sample EPA State MSW data (2018)
# In production, this would load from the actual EPA dataset
EPA_STATE_MSW_2018 = {
    "Texas": {"recycling_rate": 24.5, "total_waste_tons": 35000000},
    "California": {"recycling_rate": 42.0, "total_waste_tons": 45000000},
    "New York": {"recycling_rate": 18.0, "total_waste_tons": 32000000},
    "Florida": {"recycling_rate": 30.0, "total_waste_tons": 28000000},
    "Illinois": {"recycling_rate": 22.0, "total_waste_tons": 19000000},
    "Pennsylvania": {"recycling_rate": 20.0, "total_waste_tons": 18000000},
    "Ohio": {"recycling_rate": 25.0, "total_waste_tons": 17000000},
    "Michigan": {"recycling_rate": 19.5, "total_waste_tons": 15000000},
    "North Carolina": {"recycling_rate": 28.0, "total_waste_tons": 14000000},
    "Georgia": {"recycling_rate": 26.0, "total_waste_tons": 13000000},
}


def get_recycling_rate(state: str, year: str) -> dict | None:
    """
    Get recycling rate for a state and year.
    
    Args:
        state: US state name (e.g., "Texas")
        year: Year as string (e.g., "2018")
    
    Returns:
        Dict with 'value' (percentage) and 'year', or None if not found
    """
    if year != "2018":
        # For now, only 2018 data is available
        return None
    
    state_data = EPA_STATE_MSW_2018.get(state)
    if not state_data:
        return None
    
    return {
        "value": state_data["recycling_rate"],
        "year": year,
        "state": state,
    }

