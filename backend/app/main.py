from fastapi import FastAPI
from backend.app.routes import chat, plans
from app.routes import chat, plans
from app.routes import query, documents
from utils.db_utils import init_db

@app.on_event("startup")
async def startup_event():
    init_db()

app = FastAPI(title="Insurance LLM System")

# Include routes
app.include_router(query.router, prefix="/api/query", tags=["Query"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])

@app.get("/")
async def root():
    return {"message": "Insurance LLM API is running"}
