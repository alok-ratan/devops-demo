from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello DevOps!"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_version():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["version"] == "1.0.0"


def test_get_users():
    response = client.get("/users")

    assert response.status_code == 200
    assert response.json()["count"] >= 2


def test_get_existing_user():
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json()["name"] == "Alok"


def test_get_non_existing_user():
    response = client.get("/users/999")

    assert response.status_code == 404


def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "Test User",
            "email": "test@example.com"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Test User"