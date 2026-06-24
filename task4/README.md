# Task 4 — Containerizing the API with Docker

## Purpose

In Task 3 you built the **Patient Management API** and ran it locally with a
virtual environment. In this task you will package it so it runs the same way on
any machine — yours, a teammate's, or a server — using **Docker** and **Docker
Compose**.

You will write a `Dockerfile` for the API and a `docker-compose.yml` that runs the
API together with its supporting services (a **database** and **Redis**), wired up
with networks, volumes, and environment variables. No new application features —
the goal is to move the existing app into containers and make it start with a
single command.

This task is **README-only**. There is no scaffold: you write the Docker files
yourself, based on the requirements and resources below.

## AI Usage Rule

AI tools are allowed. Use them to explain Docker errors, review your `Dockerfile`,
or compare base images.

You must still **understand every line** of your `Dockerfile` and
`docker-compose.yml`. Be ready to explain in review why each layer, service,
volume, and environment variable exists.

## Prerequisites

- A working Task 3 API (`task3/projects/patient-api/`) that runs and passes tests.
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker
  Engine + the Compose plugin) installed. Verify:

  ```bash
  docker --version
  docker compose version
  ```

## What You Will Learn

- **Images vs. containers** — what a build produces and what runs
- Writing a **`Dockerfile`** (base image, layers, caching, `WORKDIR`, `COPY`, `CMD`)
- Keeping images small and builds fast (`.dockerignore`, layer ordering, slim base)
- **Docker Compose** — defining multiple services in one file
- **Networking** between containers (services reach each other by name)
- **Volumes** — persisting database data and bind-mounting code for development
- **Environment variables** and secrets via `.env`
- **`depends_on` + healthchecks** so services start in the right order
- Connecting the API to **PostgreSQL** and **Redis** running as containers

## The Task — Dockerize the Patient Management API

Work on a branch and place your Docker files alongside the Task 3 project (or copy
the project into `task4/` if you prefer a clean slate — your call, just explain it
in your PR).

```bash
git switch -c task4/dockerize-api
```

### 1. Move the database to PostgreSQL

SQLite is a single file and does not fit a multi-container setup well. Point the
API at PostgreSQL using the `DATABASE_URL` environment variable, for example:

```text
DATABASE_URL=postgresql+psycopg://patient:secret@db:5432/patients
```

Note the host is `db` — the **service name** from Compose, not `localhost`. Add
the matching driver (e.g. `psycopg[binary]`) to your `requirements.txt`.

### 2. Write a `Dockerfile` for the API

Your `Dockerfile` should:

- start from a slim official Python base image,
- set a working directory,
- copy `requirements.txt` and install dependencies **before** copying the rest of
  the code (so the dependency layer is cached),
- copy the application code,
- expose the API port,
- run the app with `uvicorn` (bound to `0.0.0.0`, not `127.0.0.1`).

### 3. Add a `.dockerignore`

Keep the image small and clean — exclude `.venv/`, `__pycache__/`, `.git/`,
`*.db`, `.env`, and test/cache artifacts.

### 4. Write `docker-compose.yml`

Define at least these services:

| Service | Image / build | Notes |
| --- | --- | --- |
| `api` | build from your `Dockerfile` | exposes the app port; reads env vars; `depends_on` db and redis |
| `db` | `postgres:16` (or similar) | sets `POSTGRES_*` env; persists data in a **named volume** |
| `redis` | `redis:7` (or similar) | for caching / rate limiting / background work |

Your Compose file must include:

- **Volumes** — a named volume for PostgreSQL data so it survives `docker compose down`.
- **Environment variables** — pass `DATABASE_URL`, `SECRET_KEY`, etc. (load from a `.env` file; commit only `.env.example`).
- **`depends_on` with healthchecks** — the API should wait until the database is actually ready, not just started.
- **Port mapping** — expose the API to your host (e.g. `8000:8000`).
- (Optional) a **bind mount** of your source code plus `--reload` for a smooth dev loop.

### 5. Run it

```bash
docker compose up --build
# open http://127.0.0.1:8000/docs
```

Then confirm:

```bash
docker compose ps          # all services healthy/running
docker compose logs api    # app started and connected to the database
docker compose down        # stops; data persists in the named volume
docker compose up          # data is still there
```

### 6. Use Redis for something real (optional but encouraged)

Wire Redis into the API — for example, cache a read endpoint, add simple rate
limiting, or back a background task — to prove the service is actually connected.

## Required Deliverables

1. A working `Dockerfile` for the API.
2. A `docker-compose.yml` defining `api`, `db` (PostgreSQL), and `redis`.
3. A named **volume** so database data persists across restarts.
4. A `.dockerignore` file.
5. A `.env.example` documenting every environment variable (no real secrets).
6. The API runs end-to-end with `docker compose up --build` and `/docs` works.
7. An updated project `README.md` with the Docker run instructions.

## Learning Resources

**Start here**

- [Docker — Get started](https://docs.docker.com/get-started/) — official, beginner-friendly.
- [Docker Compose — Overview](https://docs.docker.com/compose/) and the [Compose file reference](https://docs.docker.com/reference/compose-file/).

**Video courses (YouTube)**

- [Docker in 100 Seconds](https://www.youtube.com/watch?v=Gjnup-PuquQ) — Fireship; images, containers, and Dockerfiles in a nutshell before you dive in.
- [Learn Docker in 1 Hour — Full Course for Beginners](https://www.youtube.com/watch?v=GFgJkfScVNU) — fast, practical overview.
- [Docker Tutorial for Beginners (Full Course in 3 Hours)](https://www.youtube.com/watch?v=3c-iBn73dDE) — thorough fundamentals.
- [Ultimate Docker Compose Tutorial](https://www.youtube.com/watch?v=SXwC9fSwct8) — Compose from zero to hero.
- [Docker Full Course: Containers, Databases, Compose & Beyond](https://www.youtube.com/watch?v=s69slvfVp0I) — multi-service apps with databases.

**By topic**

| Topic | Resource |
| --- | --- |
| Writing a Dockerfile | [Dockerfile reference](https://docs.docker.com/reference/dockerfile/) · [Best practices](https://docs.docker.com/build/building/best-practices/) |
| FastAPI in containers | [FastAPI in Containers — Docker](https://fastapi.tiangolo.com/deployment/docker/) |
| `.dockerignore` | [Docker build context](https://docs.docker.com/build/concepts/context/#dockerignore-files) |
| PostgreSQL image | [`postgres` on Docker Hub](https://hub.docker.com/_/postgres) |
| Redis image | [`redis` on Docker Hub](https://hub.docker.com/_/redis) |
| Volumes | [Docker volumes](https://docs.docker.com/storage/volumes/) |
| Healthchecks | [Compose `healthcheck`](https://docs.docker.com/reference/compose-file/services/#healthcheck) |

## Submission Checklist

- [ ] I worked on a `task4/...` branch and committed in small, meaningful steps.
- [ ] I wrote a `Dockerfile` and can explain every instruction in it.
- [ ] `docker compose up --build` starts `api`, `db`, and `redis`, and `/docs` works.
- [ ] Database data persists across `docker compose down` / `up` via a named volume.
- [ ] I added a `.dockerignore` and a `.env.example`, and did **not** commit a real `.env` or any secrets.
- [ ] I updated the project `README.md` with Docker instructions.
- [ ] I opened a pull request into `main` with a clear description.

## Reflection

Add your reflection before submitting:

```text
1. What is the difference between an image and a container?
2. Why install dependencies before copying the rest of the code in the Dockerfile?
3. Why does the API use `db` (not `localhost`) as the database host?
4. What would happen to your data without a named volume?
5. Why use a healthcheck with `depends_on`?
6. What did Docker make easier compared to running the app with a virtualenv?
```
