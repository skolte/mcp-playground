
# MCP Playground

This project demonstrates a hands-on implementation of a Model Context Protocol (MCP) server integrated with AI agents.

## Structure
- `backend`: FastAPI-based MCP server
- `frontend`: Placeholder for React frontend dashboard

## Quickstart

### 1. Start the backend server
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2. Access context API
- `POST /get_context` with JSON `{ "agent_id": "agent1" }`
- `POST /update_context` with JSON `{ "agent_id": "agent1", "context": {"key": "value"} }`

### 3. Frontend setup (TBD)
- Scaffold React app inside `frontend/` using Vite or Create React App.
