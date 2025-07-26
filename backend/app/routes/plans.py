from fastapi import APIRouter, HTTPException
from app.utils.db_utils import get_all_plans

router = APIRouter(prefix="/plans", tags=["Plans"])

@router.get("/")
async def fetch_plans():
    """
    Fetch all insurance plans from the database.
    """
    try:
        plans = get_all_plans()
        return {"status": "success", "plans": plans}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching plans: {str(e)}")
