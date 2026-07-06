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
from app.database import Base, engine
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.middleware import LoggingMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    print("shutting down")


app = FastAPI(
    title="Patient Management API",
    description="""
    A REST API for managing patients and their medical records.
    
    ## Features
    - Patient CRUD operations
    - JWT authentication
    - Filtering and pagination
    """,
    version="1.0.0",
    license_info={"name": "MIT"},
    lifespan=lifespan,
)


@app.get("/", tags=["meta"], summary="API root")
def read_root() -> dict[str, str]:
    """Return a friendly welcome message."""
    return {"message": "Patient Management API. See /docs for the interactive docs."}


@app.get("/health", tags=["meta"], summary="Health check", status_code=200)
def health() -> dict[str, str]:
    """Return the service status. Useful for uptime checks."""
    return {"status": "ok"}


app.include_router(patients.router)
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)
