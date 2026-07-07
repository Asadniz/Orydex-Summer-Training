"""Starter test — proves the app boots and the health check works.

Run from the patient-api/ directory:
    pytest

Add your own tests (test_patients.py, test_auth.py) as you build each feature.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root_responds():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
