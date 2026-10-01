"""Application settings loaded from environment variables.

All configuration lives here. Import ``settings`` wherever you need it.
No value is hard-coded in other modules.
"""

from __future__ import annotations

import os


class Settings:
    """Minimal settings for the foundation release.

    Expand this class (or switch to pydantic-settings) when the project
    grows to need database URLs, secret keys, or third-party API tokens.
    """

    app_name: str = os.getenv("APP_NAME", "Resume AI Analyzer")
    app_version: str = "0.1.0"
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Comma-separated list of allowed CORS origins.
    # Local default: Vite dev server.
    # Production: set ALLOWED_ORIGINS=https://your-app.vercel.app on Render.
    allowed_origins: list[str] = [
        o.strip()
        for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")
        if o.strip()
    ]

    # Future: add DATABASE_URL, SECRET_KEY, AI_API_KEY, …


settings = Settings()
