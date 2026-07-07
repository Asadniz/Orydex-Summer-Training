import pytest

@pytest.fixture
def get_token(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.post(
        "/auth/token", data={"username": "asad", "password": "password123"}
    )
    return response.json()["access_token"]

@pytest.fixture
def auth_headers(get_token):
    return {"Authorization": f"Bearer {get_token}"}


def test_create_patient(client, auth_headers):
    response = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_create_patient_unauthenticated(client):
    response = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
    )
    assert response.status_code == 401


def test_get_patients(client):
    response = client.get("/patients/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_patient_by_id(client, auth_headers):
    create = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    patient_id = create.json()["id"]
    response = client.get(f"/patients/{patient_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "John"


def test_get_patient_not_found(client):
    response = client.get("/patients/999")
    assert response.status_code == 404


def test_update_patient(client, auth_headers):
    create = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    patient_id = create.json()["id"]
    response = client.put(
        f"/patients/{patient_id}",
        json={
            "name": "Jane Doe",
            "age": 25,
            "condition": "hypertension",
            "risk_score": 40,
            "active": True,
        },
        headers=auth_headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"


def test_delete_patient(client, auth_headers):
    create = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    patient_id = create.json()["id"]
    response = client.delete(f"/patients/{patient_id}", headers=auth_headers)
    assert response.status_code == 204


def test_validation_error(client, auth_headers):
    response = client.post(
        "/patients/",
        json={
            "name": "",
            "age": 200,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    assert response.status_code == 422


def test_get_patients_filter_active(client, auth_headers):
    client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    response = client.get("/patients/?active=true")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_patients_filter_condition(client, auth_headers):
    client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    response = client.get("/patients/?condition=diabetes")
    assert response.status_code == 200
    assert all(p["condition"] == "diabetes" for p in response.json())


def test_get_patients_sort_asc(client, auth_headers):
    client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    client.post(
        "/patients/",
        json={
            "name": "Anna",
            "age": 25,
            "condition": "asthma",
            "risk_score": 30,
            "active": True,
        },
        headers=auth_headers,
    )
    response = client.get("/patients/?sort=name")
    assert response.status_code == 200


def test_get_patients_sort_desc(client, auth_headers):
    client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    client.post(
        "/patients/",
        json={
            "name": "Anna",
            "age": 25,
            "condition": "asthma",
            "risk_score": 30,
            "active": True,
        },
        headers=auth_headers,
    )
    response = client.get("/patients/?sort=-name")
    assert response.status_code == 200


def test_get_patients_pagination(client, auth_headers):
    for i in range(5):
        client.post(
            "/patients/",
            json={
                "name": f"Patient {i}",
                "age": 30,
                "condition": "diabetes",
                "risk_score": 50,
                "active": True,
            },
            headers=auth_headers,
        )
    response = client.get("/patients/?limit=2&offset=0")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_update_patient_not_found(client, auth_headers):
    response = client.put(
        "/patients/999",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    assert response.status_code == 404


def test_patch_patient(client, auth_headers):
    create = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    patient_id = create.json()["id"]
    response = client.patch(
        f"/patients/{patient_id}", json={"name": "Jane"}, headers=auth_headers
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jane"


def test_patch_patient_not_found(client, auth_headers):
    response = client.patch("/patients/999", json={"name": "Jane"}, headers=auth_headers)
    assert response.status_code == 404


def test_delete_patient_not_found(client, auth_headers):
    response = client.delete("/patients/999", headers=auth_headers)
    assert response.status_code == 404


def test_validation_age_out_of_range(client, auth_headers):
    response = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 200,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers,
    )
    assert response.status_code == 422


def test_validation_missing_name(client, auth_headers):
    response = client.post(
        "/patients/",
        json={"age": 30, "condition": "diabetes", "risk_score": 50, "active": True},
        headers=auth_headers,
    )
    assert response.status_code == 422


def test_validation_risk_score_out_of_range(client, auth_headers):
    response = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 150,
            "active": True,
        },
        headers=auth_headers,
    )
    assert response.status_code == 422