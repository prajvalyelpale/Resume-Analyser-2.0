# Project State: Resume AI Analyzer

> **Single source of truth.** Update this file whenever you complete a task,
> make a significant decision, or change direction. Keep it honest and concise.

---

## Status

Foundation complete and runnable. Resume upload, analysis, AI, and database
features are not yet implemented.

---

## Architecture

```
Resume-Analyser-2.0/          ← monorepo root
├── frontend/                 React 19 · Vite 6 · TypeScript 5
│   ├── src/
│   │   ├── App.tsx           Static home page (upload placeholder)
│   │   ├── main.tsx          React entry point
│   │   └── style.css         Design tokens + layout
│   ├── vite.config.ts        Dev server + /api proxy → :8000
│   └── .env.example          Frontend env-var template
│
├── backend/                  Python 3.10+ · FastAPI · Uvicorn
│   ├── app/
│   │   ├── main.py           FastAPI app, CORS, root routes
│   │   ├── config.py         Centralised settings (reads env vars)
│   │   └── routers/
│   │       └── v1.py         /api/v1/* versioned routes
│   ├── requirements.txt      Runtime dependencies
│   └── .env.example          Backend env-var template
│
├── .gitignore
├── README.md
└── PROJECT_STATE.md          ← you are here
```

**Runtime topology (local dev):**

```
Browser → Vite :5173 → (proxy /api/*) → FastAPI :8000
```

**Planned additions (not yet implemented):**
- PostgreSQL: schema, migrations (Alembic), ORM models
- File upload endpoint + secure storage
- AI / agentic-AI analysis pipeline
- Authentication

---

## Decisions

| Decision | Rationale |
|---|---|
| Monorepo (one repo, two top-level folders) | Simple to navigate; easy to split later if needed |
| Vite dev proxy for `/api/*` | Avoids browser CORS errors in dev without disabling security |
| Central `config.py` (not `pydantic-settings` yet) | Keeps dependencies minimal; easy to migrate when the first secret appears |
| Routes versioned under `/api/v1` | Safe to evolve the API without breaking old clients |
| No database connection yet | Will be added once data requirements and security posture are defined |
| No AI libraries yet | Added only after core data pipeline and safety requirements are clear |

---

## Completed Work

- [x] Monorepo folder structure (`frontend/`, `backend/`)
- [x] React 19 + Vite 6 + TypeScript 5 frontend scaffold
- [x] Static home page with upload placeholder section and responsive design
- [x] FastAPI backend with `GET /`, `GET /health`, `GET /api/v1/status`
- [x] Central `config.py` settings module (env-var driven)
- [x] Versioned router in `backend/app/routers/v1.py`
- [x] CORS middleware (allows Vite dev server origin)
- [x] Vite dev proxy (forwards `/api/*` and `/health` to `:8000`)
- [x] `.env.example` files for both frontend and backend
- [x] Comprehensive `.gitignore` (Node, Python, editors, env files)
- [x] `README.md` with setup and run instructions
- [x] `PROJECT_STATE.md` as single source of truth

---

## Current Work

_Nothing in progress. This is the completed foundation._

---

## Next Tasks

1. **Define data requirements** – supported file formats (PDF, DOCX), max size,
   retention policy, privacy rules.
2. **PostgreSQL setup** – add `DATABASE_URL` to `.env.example`, create an
   Alembic migration, and define the first ORM model (`Resume`).
3. **File upload endpoint** – `POST /api/v1/resumes` with validation and
   secure storage (local filesystem first, cloud later).
4. **Frontend upload flow** – wire the upload placeholder to the real endpoint.
5. **Testing** – add `pytest` + `httpx` for the backend, Vitest for the
   frontend; target the happy path and error cases of each new route.
6. **AI/agentic-AI pipeline** – design only after the core data flow works and
   requirements are clear.
