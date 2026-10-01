"""Resume AI Analyzer – FastAPI application entry point.

Run locally with:
    uvicorn app.main:app --reload

Interactive API docs are available at http://localhost:8000/docs.
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import v1

app = FastAPI(
    title=settings.app_name,
    description="Backend foundation for the Resume AI Analyzer application.",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
)

# ---------------------------------------------------------------------------
# CORS – origins are controlled via the ALLOWED_ORIGINS env var.
# Local default: http://localhost:5173 (Vite dev server).
# Production: set ALLOWED_ORIGINS=https://your-app.vercel.app on Render.
# ---------------------------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(v1.router)


# ---------------------------------------------------------------------------
# Root routes (not versioned)
# ---------------------------------------------------------------------------
@app.get("/", summary="Root")
def read_root() -> dict[str, str]:
    """Return a simple greeting to confirm the API is reachable."""
    return {
        "name": settings.app_name,
        "message": "API is running.",
    }


@app.get("/health", summary="Health check")
def read_health() -> dict[str, str]:
    """Lightweight health-check endpoint for monitoring."""
    return {"status": "healthy"}
