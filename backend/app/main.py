from fastapi import FastAPI

app = FastAPI(
    title="Resume AI Analyzer API",
    description="Backend foundation for the Resume AI Analyzer application.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "name": "Resume AI Analyzer",
        "message": "API is running.",
    }


@app.get("/health")
def read_health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/api/v1/status")
def read_api_status() -> dict[str, str]:
    return {
        "status": "operational",
        "version": app.version,
    }
