"""
EcoAssist FastAPI Backend
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uuid

from rag.engine import get_rag_engine

app = FastAPI(
    title="EcoAssist API",
    description="AI-Powered RAG Assistant for Pollution Awareness & Sustainable Development",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────────
# Schemas
# ──────────────────────────────────────────────

class QueryRequest(BaseModel):
    question: str
    session_id: Optional[str] = None

class Source(BaseModel):
    title: str
    sdg: str
    tags: Optional[str] = ""

class QueryResponse(BaseModel):
    answer: str
    sources: list[Source]
    session_id: str

class ResetRequest(BaseModel):
    session_id: Optional[str] = None

# ──────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────

@app.get("/")
async def root():
    return {
        "name": "EcoAssist API",
        "version": "1.0.0",
        "status": "running",
        "sdgs": ["SDG 3", "SDG 11", "SDG 12", "SDG 13"],
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/api/chat", response_model=QueryResponse)
async def chat(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    session_id = request.session_id or str(uuid.uuid4())

    try:
        rag = get_rag_engine()
        result = rag.query(request.question, session_id)
        return QueryResponse(
            answer=result["answer"],
            sources=[Source(**s) for s in result["sources"]],
            session_id=session_id,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/reset")
async def reset_conversation(request: ResetRequest):
    try:
        rag = get_rag_engine()
        rag.reset_memory()
        return {"status": "ok", "message": "Conversation memory cleared."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/topics")
async def get_topics():
    """Return all SDG topics available in the knowledge base."""
    from knowledge_base.sdg_knowledge import SDG_DOCUMENTS
    topics = [
        {
            "id": doc["id"],
            "title": doc["title"],
            "sdg": doc["sdg"],
            "tags": doc["tags"],
        }
        for doc in SDG_DOCUMENTS
    ]
    return {"topics": topics, "count": len(topics)}
