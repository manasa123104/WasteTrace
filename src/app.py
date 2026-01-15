from fastapi import FastAPI
from pydantic import BaseModel

from src.utils.answer import format_summary
from src.utils.router import route_query

app = FastAPI(title="WasteTrace API", version="0.1.0")


class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/query")
def query_waste(request: QueryRequest) -> dict:
    route = route_query(request.question)
    summary = format_summary(request.question, route)
    return {"route": route, "summary": summary}

