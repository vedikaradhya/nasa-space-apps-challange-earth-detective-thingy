# Backend README

This backend contains skeleton code for the NASA data connectors, GitHub OAuth routes, Postgres models, and Celery integration.

Environment

- DATABASE_URL (postgresql://user:pass@host:port/dbname)
- REDIS_URL (redis://host:port/0)
- GITHUB_CLIENT_ID
- GITHUB_CLIENT_SECRET
- NASA_API_KEY
- SECRET_KEY (app secret for cookies/sessions)

Run locally (quick):

1. python -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. uvicorn app.main:app --reload --port 8000

Notes
- Alembic migrations not included; see db.py and models.py for SQLModel/SQLAlchemy usage.
