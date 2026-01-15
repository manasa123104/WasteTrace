import json
import sys

from src.utils.answer import format_summary
from src.utils.router import route_query


def handle_request(payload: dict) -> dict:
    method = payload.get("method")
    if method == "list_tools":
        return {
            "tools": [
                {
                    "name": "wastetrace.query",
                    "description": "Route a waste analytics question.",
                    "input_schema": {"type": "object", "properties": {"question": {"type": "string"}}},
                }
            ]
        }
    if method == "call_tool":
        tool = payload.get("tool")
        args = payload.get("args", {})
        if tool == "wastetrace.query":
            route = route_query(args.get("question", ""))
            summary = format_summary(args.get("question", ""), route)
            return {"route": route, "summary": summary}
        return {"error": f"Unknown tool: {tool}"}
    return {"error": f"Unknown method: {method}"}


def main() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
            response = handle_request(payload)
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON payload"}
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

