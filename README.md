# IA Site

Plateforme full-stack pour générer, gérer et administrer des projets web à partir de besoins en langage naturel.

## Stack
- Frontend: React + Vite + TailwindCSS
- Backend: FastAPI + SQLAlchemy
- DB: PostgreSQL (prod) / SQLite (dev)
- Auth: JWT access + refresh
- Tests: Pytest

## Fonctionnalités principales
- Authentification (register/login/logout/refresh)
- RBAC (Admin/User) avec contrôle côté serveur
- CRUD projets avec recherche + pagination
- Dashboard admin (stats, gestion utilisateurs, logs)
- Upload d'images en local (dev)
- Générateur IA (templates + prompting + génération de scaffolds)

## Architecture
```
frontend -> backend (FastAPI) -> database (PostgreSQL/SQLite)
```

## Démarrage rapide (local)

### Backend
```bash
cd backend
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
cp .env.example .env
npm install
npm run dev
```

### Tests
```bash
cd backend
pytest
```

## Docker (prod-like)
```bash
docker compose up --build
```

## Variables d'environnement
### Backend
- `SECRET_KEY`
- `DATABASE_URL`
- `BACKEND_CORS_ORIGINS`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `REFRESH_TOKEN_EXPIRE_MINUTES`
- `RATE_LIMIT_LOGIN`
- `UPLOAD_DIR`

### Frontend
- `VITE_API_URL`

## Endpoints API (exemples)
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `GET /api/v1/projects?query=...`
- `POST /api/v1/projects`
- `GET /api/v1/admin/stats`
- `POST /api/v1/ai/generate`

## Génération IA
Le moteur IA combine des templates locaux et, si configuré, un modèle OpenAI pour produire un résumé et des fichiers prêts à l'emploi.

Variables nécessaires :
- `AI_PROVIDER=local` ou `openai`
- `AI_MODEL=gpt-4o-mini`
- `OPENAI_API_KEY` (si provider OpenAI)
