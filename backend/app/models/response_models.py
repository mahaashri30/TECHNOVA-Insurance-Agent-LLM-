from pydantic import BaseModel
from typing import List, Dict, Optional

# ✅ For referencing clauses in the response
class ClauseReference(BaseModel):
    clause: str
    source: str

# ✅ For the AI decision response
class DecisionResponse(BaseModel):
    decision: str  # e.g., "approved" or "rejected"
    amount: Optional[str] = None  # e.g., "50000 INR"
    justification: List[ClauseReference]

# ✅ For incoming user queries
class ChatRequest(BaseModel):
    query: str  # Natural language query from user
    user_profile: Optional[Dict] = None  # Optional user info like age, location

# ✅ For document upload API
class DocumentUploadResponse(BaseModel):
    message: str
    total_documents_indexed: int
