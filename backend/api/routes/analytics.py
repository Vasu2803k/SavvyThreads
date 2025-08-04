"""
Analytics router for the SavvyThreads API.
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from fastapi import APIRouter
from scripts.log_config import get_logger

router = APIRouter(
    prefix="/api/v1/analytics",
    tags=["Analytics"]
)
logger = get_logger(__name__)

@router.get("/", response_model=dict)
async def analytics_overview() -> dict:
    logger.info("Analytics endpoint accessed.")
    return {"message": "Analytics endpoint placeholder"} 