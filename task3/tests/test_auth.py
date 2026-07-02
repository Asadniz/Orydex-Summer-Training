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


def test_login_wrong_password(client):
    client.post("/auth/register", json={"username": "asad", "password": "password123"})
    response = client.post(
        "/auth/token", data={"username": "asad", "password": "wrongpassword"}
    )
    assert response.status_code == 401
