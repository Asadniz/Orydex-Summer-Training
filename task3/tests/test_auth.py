def test_register(client):
    response = client.post(
        "/auth/register", json={"username": "asad", "password": "password123"}
    )
    assert response.status_code == 201
    assert response.json()["username"] == "asad"


def test_register_duplicate(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.post(
        "/auth/register", json={"username": "asad", "password": "password123"}
    )
    assert response.status_code == 409


def test_login(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.post(
        "/auth/token", data={"username": "asad", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_notregistered_user(client):
    response = client.post(
        "/auth/token", data={"username": "doesnotexist", "password": "password123"}
    )
    assert response.status_code == 401


def test_login_wrong_password(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.post(
        "/auth/token", data={"username": "asad", "password": "wrongpassword"}
    )
    assert response.status_code == 401


def test_token_user_not_in_db(client):
    from app.auth import create_access_token

    token = create_access_token("nonexistentuser")
    response = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 401


def test_get_user(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.get("/auth/1")
    assert response.status_code == 200
    assert response.json()["username"] == "asad"


def test_token_missing_username_field(client):
    import jwt as pyjwt
    import os

    token = pyjwt.encode({"sub": "someone"}, os.getenv("secret_key"), algorithm="HS256")
    response = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 401


def test_get_user_not_found(client):
    response = client.get("/auth/999")
    assert response.status_code == 404


def test_invalid_token(client):
    response = client.post(
        "/patients/",
        json={
            "name": "John",
            "age": 30,
            "condition": "diabetes",
            "risk_score": 50,
            "active": True,
        },
        headers={"Authorization": "Bearer invalidtoken"},
    )
    assert response.status_code == 401
