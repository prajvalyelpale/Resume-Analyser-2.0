# Resume AI Analyzer

A small monorepo foundation for a resume feedback application. The current frontend is static, and the backend exposes basic service-status routes. Resume processing, AI features, and PostgreSQL integration are not implemented yet.

## Project Structure

```text
frontend/                 React + Vite + TypeScript application
	src/                    Page and styles
backend/                  FastAPI application
	app/main.py             API app and starter routes
	requirements.txt        Python dependencies
PROJECT_STATE.md           Project status, architecture, decisions, and next tasks
```

## Requirements

- Node.js 18+ and npm
- Python 3.10+
- PostgreSQL is planned, but is not required to run this foundation

## Run the Frontend

```powershell
cd frontend
npm install
npm run dev
```

Open the local URL printed by Vite (normally `http://localhost:5173`). To create a production build, run `npm run build` from `frontend/`.

## Run the Backend

From the repository root, create and activate a virtual environment, then install the backend dependencies:

```powershell
cd backend
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. Interactive API documentation is at `http://localhost:8000/docs`.

Starter routes:

- `GET /`
- `GET /health`
- `GET /api/v1/status`

The frontend and API currently run independently; no database or AI connection is configured.

## Project Tracking

See [PROJECT_STATE.md](PROJECT_STATE.md) for the single source of truth on project status, architecture, decisions, completed work, and next tasks.
