"""FastAPI application entry point."""

from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db

app = FastAPI(
    title="Trading Agents API",
    description="Backend API for trading agents with LangChain",
    version="0.1.0",
)


@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    """Health check endpoint; verifies DB connectivity."""
    try:
        await db.execute(text("SELECT 1"))
    except Exception:
        return {"status": "error", "database": "unhealthy"}
    return {"status": "ok"}


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Trading Agents API", "docs": "/docs"}
