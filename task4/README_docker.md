## Running with Docker

### Prerequisites

- Docker Desktop installed and running

### Setup

1. Copy `.env.example` to `.env` and fill in your values
2. Run the app:

```bash
   docker compose up --build
```

3. Open http://127.0.0.1:8000/docs

### Other commands

```bash
docker compose ps        # check service status
docker compose logs api  # view api logs
docker compose down      # stop services (data persists)
docker compose down -v   # stop and wipe data
```
