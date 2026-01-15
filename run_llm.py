from src.utils.answer import format_summary
from src.utils.router import route_query


def main() -> None:
    question = input("Ask WasteTrace: ").strip()
    if not question:
        print("No question provided.")
        return
    route = route_query(question)
    summary = format_summary(question, route)
    print(summary)


if __name__ == "__main__":
    main()

