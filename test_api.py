from fastapi.testclient import TestClient

from api import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Laboratory work 8"
    }


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Выполнить лабораторную №8"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Выполнить лабораторную №8"


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
