
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_store: Dict[str, Any] = {}

class ContextRequest(BaseModel):
    agent_id: str

class ContextUpdate(BaseModel):
    agent_id: str
    context: Dict[str, Any]

@app.post("/get_context")
async def get_context(req: ContextRequest):
    return {"context": memory_store.get(req.agent_id, {})}

@app.post("/update_context")
async def update_context(update: ContextUpdate):
    memory_store[update.agent_id] = update.context
    return {"message": "Context updated successfully"}
