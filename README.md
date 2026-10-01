# Resume AI Analyzer

A monorepo foundation for a resume feedback application.  
**Stack:** React 19 · Vite 6 · TypeScript 5 (frontend) · Python FastAPI · Uvicorn (backend) · PostgreSQL (planned).

The current frontend is a static home page with an upload placeholder.  
The backend exposes basic service-status routes.  
Resume processing, AI features, and PostgreSQL integration are not yet implemented.

---

## Project Structure

```
Resume-Analyser-2.0/
├── frontend/                 React + Vite + TypeScript SPA
│   ├── src/
│   │   ├── App.tsx           Home page component
│   │   ├── main.tsx          React entry point
│   │   └── style.css         Design system + layout
│   ├── index.html
│   ├── vite.config.ts        Dev server config + API proxy
│   ├── package.json
│   └── .env.example          Frontend env-var template
│
├── backend/                  FastAPI application
│   ├── app/
│   │   ├── main.py           App factory, CORS, root routes
│   │   ├── config.py         Settings (reads environment variables)
│   │   └── routers/
│   │       └── v1.py         /api/v1/* endpoints
│   ├── requirements.txt      Python runtime dependencies
│   └── .env.example          Backend env-var template
│
├── .gitignore
├── README.md                 ← you are here
└── PROJECT_STATE.md          Architecture, decisions, task tracking
```

---

## Requirements

| Tool | Minimum version |
|---|---|
| Node.js | 18 |
| npm | 9 |
| Python | 3.10 |
| PostgreSQL | 15 _(not required for the foundation)_ |

---

## Run the Frontend

```powershell
cd frontend
npm install        # first time only
npm run dev
```

Open **http://localhost:5173** in your browser.  
The dev server proxies `/api/*` and `/health` requests to the backend on `:8000`, so you can run both simultaneously without browser CORS issues.

To create a production build:
```powershell
npm run build      # outputs to frontend/dist/
```

---

## Run the Backend

```powershell
cd backend
py -m venv .venv                     # create virtual environment
.venv\Scripts\Activate.ps1           # activate (PowerShell)
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API is available at **http://localhost:8000**.  
Interactive docs: **http://localhost:8000/docs**

### Available routes

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Root – confirms the API is running |
| `GET` | `/health` | Lightweight health check |
| `GET` | `/api/v1/status` | Versioned status + version string |

---

## Environment Variables

Copy the example files and fill in real values before running:

```powershell
# Backend
copy backend\.env.example backend\.env

# Frontend (optional – proxy handles local dev)
copy frontend\.env.example frontend\.env.local
```

Both `.env` and `.env.local` are git-ignored.

---

## Project Tracking

See [PROJECT_STATE.md](PROJECT_STATE.md) for the single source of truth on
project status, architecture, decisions, completed work, and next tasks.
