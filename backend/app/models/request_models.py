from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    age: int
    gender: str
    location: str
    existing_conditions: List[str]
    policy_start_date: str
    query: str

class ChatRequest(BaseModel):
    query: str
    user_profile: dict  # Use dict unless you want a structured model
