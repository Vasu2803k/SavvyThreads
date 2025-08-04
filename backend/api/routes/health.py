"""
Health router for the SavvyThreads API.
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from fastapi import APIRouter
from scripts.log_config import get_logger

router = APIRouter(
    prefix="/api/v1/health",
    tags=["Health"]
)
logger = get_logger(__name__)

@router.get("/", response_model=dict)
async def health() -> dict:
    logger.info("Health endpoint accessed.")
    return {"status": "SavvyThreads API v1 is running"} 