"""
Ingest router for the SavvyThreads API.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from fastapi import APIRouter, HTTPException, status
from api.models import IngestRequest
from tools.ingest_tool import IngestTool
from scripts.log_config import get_logger

router = APIRouter(
    prefix="/api/v1/ingest",
    tags=["Ingest"]
)
logger = get_logger(__name__)

@router.post("/", response_model=dict)
async def ingest(request: IngestRequest) -> dict:
    try:
        logger.info(f"Received ingest request: {request}")
        ingest_tool = IngestTool()
        response = await ingest_tool.ingest(request.source, request.payload)
        logger.info(f"Ingest response: {response}")
        return response
    except Exception as e:
        logger.error(f"Ingest error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))