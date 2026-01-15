from typing import Any

import requests


def get_json(url: str, timeout_seconds: int = 10) -> dict[str, Any]:
    response = requests.get(url, timeout=timeout_seconds)
    response.raise_for_status()
    return response.json()

