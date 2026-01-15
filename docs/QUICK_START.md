Quick Start
===========

Setup
-----
1) Install dependencies:
   - uv sync
   - or: pip install -r requirements.txt
2) Run the API:
   - uvicorn src.app:app --reload
3) Run the UI:
   - streamlit run streamlit_app.py

MCP stdio server
----------------
Run:
  - python mcp_server_stdio.py

Send JSON lines:
  - {"method":"list_tools"}
  - {"method":"call_tool","tool":"wastetrace.query","args":{"question":"recycling rate in Metroville"}}

