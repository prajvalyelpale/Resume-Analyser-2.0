"""v1 API router.

All versioned endpoints live here and are mounted at /api/v1 in main.py.
Add new feature routers (e.g. resumes, analysis) as separate modules and
include them below.
"""

from __future__ import annotations

from fastapi import APIRouter

from app.config import settings

router = APIRouter(prefix="/api/v1")


@router.get("/status", summary="API v1 status")
def api_v1_status() -> dict[str, str]:
    """Return the current operational status and API version."""
    return {
        "status": "operational",
        "version": settings.app_version,
        "api": "v1",
    }
