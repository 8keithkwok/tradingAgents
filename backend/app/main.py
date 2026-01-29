"""FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="Trading Agents API",
    description="Backend API for trading agents with LangChain",
    version="0.1.0",
)


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Trading Agents API", "docs": "/docs"}
