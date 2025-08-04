"""
Chat router for the SavvyThreads API.
"""

import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from fastapi import APIRouter, HTTPException, status
from api.models import UserRequest, ChatResponse
from scripts.log_config import get_logger

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["Chat"]
)
logger = get_logger(__name__)

@router.post("/", response_model=ChatResponse)
async def chat(request: UserRequest) -> ChatResponse:
    try:
        logger.info(f"Received chat request: {request}")
        response = ChatResponse(response="Hello, world!")
        logger.info(f"Chat response: {response}")
        return response
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

