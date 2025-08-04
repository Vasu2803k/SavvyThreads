# SavvyThreads

A social knowledge graph system for analyzing and connecting communication data.

## Current Status

This is a simplified version of the SavvyThreads project with the following components:

### Backend (FastAPI)
- **API Routes**: Chat, Health, Analytics, and Ingest endpoints
- **Core**: LangGraph orchestrator and state management (currently empty)
- **Tools**: Placeholder implementations for data ingestion
- **Logging**: Centralized logging configuration

### Project Structure
```
SavvyThreads/
├── backend/          # FastAPI backend with routes and core components
│   ├── api/          # API routes and models
│   ├── core/         # LangGraph orchestrator and agents (empty)
│   └── tools/        # Tool implementations
├── scripts/          # Utility scripts (logging configuration)
├── logs/             # Application logs
├── docs/             # Documentation and architecture diagrams
├── notebooks/        # Jupyter notebooks (empty)
├── prompt_engineering/ # Prompt engineering experiments (empty)
├── graphdb/          # Graph database schemas and queries (empty)
├── frontend/         # Frontend application (empty)
└── project_structure.txt  # Current project structure
```

## Getting Started

1. **Install Dependencies**:
   ```bash
   cd backend
   pip install -e .
   ```

2. **Run the API**:
   ```bash
   cd backend
   uvicorn api.main:app --reload
   ```

3. **API Endpoints**:
   - `GET /` - Root endpoint
   - `POST /api/v1/chat/` - Chat endpoint
   - `GET /api/v1/health/` - Health check
   - `GET /api/v1/analytics/` - Analytics endpoint
   - `POST /api/v1/ingest/` - Data ingestion endpoint

## Project Components

### ✅ Implemented
- **FastAPI Backend**: Working API with 4 endpoints
- **Logging System**: Centralized logging configuration
- **Pydantic Models**: Request/response validation
- **Documentation**: Architecture diagrams and project structure

### 📁 Empty Directories (Ready for Development)
- **notebooks/**: For data analysis and experiments
- **prompt_engineering/**: For LLM prompt optimization
- **graphdb/**: For Neo4j schemas and queries
- **frontend/**: For React/UI components

### 📄 Empty Files
- **docker-compose.yml**: Docker configuration (ready to be implemented)

## Next Steps

The following components are planned but not yet implemented:
- LangChain ReAct agents with tools
- Neo4j graph database integration
- Frontend React application
- Advanced data processing and analytics
- Email/Slack/Teams integration

## Development

This project uses:
- **FastAPI** for the backend API
- **LangChain** for AI/LLM integration
- **LangGraph** for orchestration
- **Pydantic** for data validation
- **Python 3.10+** for development
