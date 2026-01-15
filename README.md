WasteTrace
==========

WasteTrace is a municipal waste analytics platform with MCP-based tools and
LLM-ready querying. It helps cities analyze waste streams, recycling rates,
and optimization opportunities across time and geography.

## Architecture

For detailed architecture documentation and diagrams, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                          │
│  "Recycling rate in Texas 2018"                            │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│  FRONTEND LAYER                                             │
│  ┌──────────────┐                                           │
│  │ Streamlit UI │  Port: 8501                              │
│  │ (User Input) │                                           │
│  └──────┬───────┘                                           │
└─────────┼───────────────────────────────────────────────────┘
          │ HTTP POST /query
          ▼
┌─────────────────────────────────────────────────────────────┐
│  API LAYER                                                  │
│  ┌──────────────┐                                           │
│  │ FastAPI      │  Port: 8000                               │
│  │ Server       │                                           │
│  └──────┬───────┘                                           │
└─────────┼───────────────────────────────────────────────────┘
          │ Route Query
          ▼
┌─────────────────────────────────────────────────────────────┐
│  PROCESSING LAYER                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Query Router │→ │   Intent     │  │ State/Year   │     │
│  │              │  │  Extractor   │  │   Parser     │     │
│  └──────┬───────┘  └──────────────┘  └──────────────┘     │
└─────────┼───────────────────────────────────────────────────┘
          │ Extract: state="Texas", year="2018", intent="recycling_rate"
          ▼
┌─────────────────────────────────────────────────────────────┐
│  DATA LAYER                                                 │
│  ┌──────────────┐      ┌──────────────────────┐           │
│  │ EPA Pipeline │◄─────┤ EPA State MSW Dataset│           │
│  │              │      │ (10 States, 2018)     │           │
│  └──────┬───────┘      └──────────────────────┘           │
│         │ Returns: {"value": 24.5, "year": "2018"}         │
│         ▼                                                   │
│  ┌──────────────┐                                           │
│  │   Answer     │  Format: "Recycling rate for Texas...    │
│  │  Formatter   │           24.5% (EPA State MSW dataset)" │
│  └──────┬───────┘                                           │
└─────────┼───────────────────────────────────────────────────┘
          │ Formatted Response
          ▼
┌─────────────────────────────────────────────────────────────┐
│                    USER SEES RESULT                          │
│  "Recycling rate for Texas in 2018: 24.5%"                  │
└─────────────────────────────────────────────────────────────┘
```

Key features
------------
- FastAPI API for waste stream analytics
- Streamlit UI for interactive exploration
- EPA State MSW dataset integration (2018 data for 10 US states)
- MCP stdio server for tool access
- Natural language query processing
- Real recycling rate data retrieval

Quick start
-----------
1) Create a virtual environment and install dependencies:
   - uv sync
   - or: pip install -r requirements.txt
2) Run the API:
   - uvicorn src.app:app --reload
3) Run the UI:
   - streamlit run streamlit_app.py
4) Run MCP server (stdio):
   - python mcp_server_stdio.py

Project layout
--------------
- src/                 API, pipelines, and core utilities
- streamlit_app.py     UI app
- mcp_server_stdio.py  MCP stdio server (source of truth)
- run_llm.py           LLM integration harness
- docs/                Documentation

