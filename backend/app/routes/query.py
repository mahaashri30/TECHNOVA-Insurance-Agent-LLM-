from fastapi import APIRouter
from models.request_models import QueryRequest
from services.query_parser import parse_query
from services.retrieval_service import retrieve_relevant_clauses
from services.decision_engine import make_decision

router = APIRouter()

@router.post("/")
async def handle_query(req: QueryRequest):
    # Parse query into structured details
    structured_data = parse_query(req.query)

    # Retrieve relevant clauses from vector DB
    clauses = retrieve_relevant_clauses(req.query)

    # Make decision using LLM
    decision = make_decision(req.query, structured_data, clauses)

    return decision
