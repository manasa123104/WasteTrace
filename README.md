WasteTrace
==========

WasteTrace is a municipal waste analytics platform with MCP-based tools and
LLM-ready querying. It helps cities analyze waste streams, recycling rates,
and optimization opportunities across time and geography.

Key features
------------
- FastAPI API for waste stream analytics
- Streamlit UI for interactive exploration
- DuckDB for local analytical storage
- MCP stdio server for tool access
- Baseline LLM harness for natural language queries

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

