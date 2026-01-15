import pandas as pd


def load_sample_data() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"city": "Metroville", "year": 2023, "recycling_rate": 0.42},
            {"city": "Metroville", "year": 2024, "recycling_rate": 0.45},
            {"city": "Greenside", "year": 2023, "recycling_rate": 0.55},
        ]
    )

