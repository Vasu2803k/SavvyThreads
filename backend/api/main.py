import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from fastapi import FastAPI
from api.routes.chat import router as chat_router
from api.routes.health import router as health_router
from api.routes.analytics import router as analytics_router
from api.routes.ingest import router as ingest_router
from scripts.log_config import setup_logging, get_logger

setup_logging(task_type="api")
logger = get_logger(__name__)
logger.info("Starting SavvyThreads API")
app = FastAPI(title="SavvyThreads-API", version="1.0.0", description="FastAPI backend for SavvyThreads")

@app.get("/", tags=["Root"], response_model=dict)
async def root() -> dict:
    logger.info("Root endpoint accessed.")
    return {"message": "Welcome to SavvyThreads API"}

app.include_router(ingest_router)
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(analytics_router) 
