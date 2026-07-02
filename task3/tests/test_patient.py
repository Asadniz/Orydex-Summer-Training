def get_token(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.post(
        "/auth/token", data={"username": "asad", "password": "password123"}
    )
    return response.json()["access_token"]


def auth_headers(client):
    token = get_token(client)
    return {"Authorization": f"Bearer {token}"}


def test_create_patient(client):
    response = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers(client),
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


def test_get_patient_not_found(client):
    response = client.get("/patients/999")
    assert response.status_code == 404


def test_update_patient(client):
    headers = auth_headers(client)
    create = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=headers,
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
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"


def test_delete_patient(client):
    headers = auth_headers(client)
    create = client.post(
        "/patients/",
        json={
            "name": "John Doe",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=headers,
    )
    patient_id = create.json()["id"]
    response = client.delete(f"/patients/{patient_id}", headers=headers)
    assert response.status_code == 204


def test_validation_error(client):
    response = client.post(
        "/patients/",
        json={
            "name": "",
            "age": 200,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers=auth_headers(client),
    )
    assert response.status_code == 422
