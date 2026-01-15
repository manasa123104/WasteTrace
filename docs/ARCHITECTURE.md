# WasteTrace Architecture

## System Overview

WasteTrace is a municipal waste analytics platform that combines FastAPI backend, Streamlit frontend, and MCP (Model Context Protocol) integration for natural language querying of EPA waste data.

## Architecture Diagram

### System Flow Diagram

```mermaid
flowchart TD
    Start([User Enters Question]) --> UI[Streamlit UI<br/>streamlit_app.py]
    
    UI -->|POST /query| API[FastAPI Server<br/>src/app.py]
    
    API -->|Process Query| Router[Query Router<br/>src/utils/router.py]
    
    Router -->|Extract Intent| Intent[Intent Extractor<br/>src/utils/intent.py]
    Router -->|Extract State| StateParser[State Parser]
    Router -->|Extract Year| YearParser[Year Parser<br/>2015-2024]
    
    Intent -->|Intent Type| Router
    StateParser -->|State Name| Router
    YearParser -->|Year Value| Router
    
    Router -->|Route to Dataset| Pipeline[EPA State MSW Pipeline<br/>src/pipelines/epa_state_msw.py]
    
    Pipeline -->|Query Data| EPA[(EPA State MSW Dataset<br/>2018 Data)]
    EPA -->|Return Data| Pipeline
    
    Pipeline -->|Raw Data| Answer[Answer Formatter<br/>src/utils/answer.py]
    
    Answer -->|Formatted Response| API
    API -->|Display Result| UI
    UI --> End([User Sees Answer])
    
    subgraph MCP[Alternative: MCP Integration]
        MCP_Server[MCP Stdio Server<br/>mcp_server_stdio.py]
        LLM[LLM Client]
        MCP_Server <-->|JSON-RPC| LLM
        MCP_Server -->|Tool Calls| Router
    end
    
    style Start fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    style End fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px
    style UI fill:#ff6a00,stroke:#333,stroke-width:3px,color:#fff
    style API fill:#1e0536,stroke:#333,stroke-width:3px,color:#fff
    style Router fill:#5b0e2d,stroke:#333,stroke-width:3px,color:#fff
    style Pipeline fill:#7dd3fc,stroke:#0277bd,stroke-width:3px,color:#000
    style Answer fill:#7dd3fc,stroke:#0277bd,stroke-width:3px,color:#000
    style EPA fill:#1565c0,stroke:#0d47a1,stroke-width:3px,color:#fff
    style MCP fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style MCP_Server fill:#ffd166,stroke:#333,stroke-width:2px,color:#000
    style LLM fill:#ffd166,stroke:#333,stroke-width:2px,color:#000
```

### Component Architecture

```mermaid
graph LR
    subgraph Frontend["🖥️ Frontend Layer"]
        UI[Streamlit UI<br/>Port: 8501]
    end
    
    subgraph API["⚙️ API Layer"]
        FastAPI[FastAPI Server<br/>Port: 8000<br/>/query endpoint]
    end
    
    subgraph Processing["🔍 Processing Layer"]
        Router[Query Router]
        Intent[Intent Extractor]
        Parser[State/Year Parser]
    end
    
    subgraph Data["💾 Data Layer"]
        Pipeline[EPA Pipeline]
        Formatter[Answer Formatter]
    end
    
    subgraph External["📊 External Data"]
        EPA[EPA Dataset<br/>10 States, 2018]
    end
    
    subgraph MCP["🔌 MCP Layer"]
        MCP_Server[MCP Server]
        LLM_Client[LLM Client]
    end
    
    UI -->|HTTP Request| FastAPI
    FastAPI -->|Route| Router
    Router --> Intent
    Router --> Parser
    Router -->|Call| Pipeline
    Pipeline -->|Query| EPA
    Pipeline -->|Data| Formatter
    Formatter -->|Response| FastAPI
    FastAPI -->|JSON| UI
    
    MCP_Server -.->|Tool Calls| Router
    MCP_Server <-->|JSON-RPC| LLM_Client
    
    style Frontend fill:#ff6a00,stroke:#333,stroke-width:2px,color:#fff
    style API fill:#1e0536,stroke:#333,stroke-width:2px,color:#fff
    style Processing fill:#5b0e2d,stroke:#333,stroke-width:2px,color:#fff
    style Data fill:#7dd3fc,stroke:#0277bd,stroke-width:2px,color:#000
    style External fill:#1565c0,stroke:#0d47a1,stroke-width:2px,color:#fff
    style MCP fill:#ffd166,stroke:#f57f17,stroke-width:2px,color:#000
```

## Component Details

### 1. Frontend Layer
- **Streamlit UI** (`streamlit_app.py`)
  - User interface with colorful gradient design
  - Accepts natural language questions
  - Displays routing information and formatted answers
  - Runs on `http://localhost:8501`

### 2. API Layer
- **FastAPI Server** (`src/app.py`)
  - RESTful API endpoints
  - `/health` - Health check
  - `/query` - Main query endpoint
  - Runs on `http://127.0.0.1:8000`

### 3. Processing Layer
- **Query Router** (`src/utils/router.py`)
  - Extracts state names from questions
  - Extracts years (2015-2024)
  - Routes to appropriate dataset based on intent
  
- **Intent Extractor** (`src/utils/intent.py`)
  - Identifies user intent:
    - `recycling_rate` - Recycling rate queries
    - `landfill_share` - Landfill percentage queries
    - `organic_diversion` - Organic waste queries
    - `plastic_stream` - Plastic waste queries
    - `waste_overview` - General waste overview

### 4. Data Layer
- **EPA State MSW Pipeline** (`src/pipelines/epa_state_msw.py`)
  - Contains 2018 recycling rate data for 10 US states
  - Returns real numeric values for supported queries
  - States: Texas, California, New York, Florida, Illinois, Pennsylvania, Ohio, Michigan, North Carolina, Georgia

- **Answer Formatter** (`src/utils/answer.py`)
  - Formats responses with real data when available
  - Falls back to routing summary for unsupported queries
  - Returns structured responses

### 5. MCP Layer
- **MCP Stdio Server** (`mcp_server_stdio.py`)
  - Implements Model Context Protocol
  - Exposes `wastetrace.query` tool
  - Enables LLM integration via stdio
  - JSON-RPC communication

## Data Flow

1. **User Input**: User enters question in Streamlit UI
   - Example: "Recycling rate in Texas 2018"

2. **API Processing**: FastAPI receives query and routes to Query Router
   - Router extracts: state="Texas", year="2018", intent="recycling_rate"

3. **Data Retrieval**: Router calls EPA State MSW Pipeline
   - Pipeline looks up Texas 2018 data
   - Returns: `{"value": 24.5, "year": "2018", "state": "Texas"}`

4. **Response Formatting**: Answer Formatter creates user-friendly response
   - Output: "Recycling rate for Texas in 2018: 24.5% (EPA State MSW dataset)."

5. **Display**: Streamlit UI displays formatted answer to user

## Technology Stack

- **Backend**: FastAPI + Uvicorn
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Protocol**: MCP (Model Context Protocol)
- **Database**: In-memory data structures (ready for DuckDB integration)

## File Structure

```
wastetrance main/
├── src/
│   ├── app.py                    # FastAPI server
│   ├── pipelines/
│   │   ├── epa_state_msw.py      # EPA data pipeline
│   │   └── waste_streams.py      # Waste streams pipeline
│   └── utils/
│       ├── router.py             # Query routing
│       ├── intent.py              # Intent extraction
│       ├── answer.py              # Answer formatting
│       └── ...
├── streamlit_app.py               # Streamlit UI
├── mcp_server_stdio.py            # MCP server
├── run_llm.py                     # LLM harness
└── docs/
    ├── ARCHITECTURE.md            # This file
    ├── MCP_ARCHITECTURE.md        # MCP details
    └── QUICK_START.md             # Setup guide
```

## Future Enhancements

- [ ] DuckDB integration for larger datasets
- [ ] Additional EPA datasets (landfill, composting)
- [ ] Multi-year data support (2015-2024)
- [ ] City-level granularity
- [ ] Comparison queries (state vs state)
- [ ] Trend analysis over time
- [ ] Visualization charts
- [ ] Authentication and user management

