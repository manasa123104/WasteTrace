MCP Architecture
================

WasteTrace exposes an MCP stdio server that returns tools and routes questions
to waste analytics intents. The tool surface is intentionally minimal:

- wastetrace.query: routes a natural language question to a dataset, intent, and
  default granularity.

The MCP server is implemented in `mcp_server_stdio.py` and is designed to be
easy to extend with additional tools, datasets, or storage backends.

