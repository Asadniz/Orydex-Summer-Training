"""Patient Management API — starter app.

This is your starting point for Task 3. It boots and exposes two endpoints so
you can confirm your environment works. Build the rest of the API on top of it,
following the day-by-day blocks in task3/README.md.

Run it:
    uvicorn app.main:app --reload
Then open the interactive docs at http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from app.routers import patients, auth
from app.models import patient, user
from app.database import Base, engine, get_session

app = FastAPI(
    title="Patient Management API",
    description="Training capstone for Task 3 (FastAPI).",
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

@app.get("/", tags=["meta"], summary="API root")
def read_root() -> dict[str, str]:
    """Return a friendly welcome message."""
    return {"message": "Patient Management API. See /docs for the interactive docs."}


@app.get("/health", tags=["meta"], summary="Health check", status_code=200)
def health() -> dict[str, str]:
    """Return the service status. Useful for uptime checks."""
    return {"status": "ok"}


# TODO: create app/routers/patients.py and register it here, e.g.

app.include_router(patients.router)
app.include_router(auth.router)
