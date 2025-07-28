from fastapi import FastAPI
from app.routes import query, documents
from app.utils.db_utils import init_db

app = FastAPI(title="Insurance LLM System")

@app.on_event("startup")
async def startup_event():
    init_db()

# Include route handlers
app.include_router(query.router, prefix="/api/query", tags=["Query"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])

@app.get("/")
async def root():
    return {"message": "Insurance LLM API is running"}
