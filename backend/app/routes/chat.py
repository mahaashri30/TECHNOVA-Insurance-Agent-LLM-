from fastapi import APIRouter, HTTPException
from app.models.request_models import QueryRequest
from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse
from app.services.llm_service import generate_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
async def chat_endpoint(req: ChatRequest):
    """
    Handles user queries related to insurance.
    """
    try:
        response = await generate_response(query=req.query, user_profile=req.user_profile)
        return {"status": "success", "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
