from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_retrieve_task_happy_path():
    retrieve_payload = {
    "task_id": "T-001",
    "type": "retrieve",
    "ndc": "NDC_0001",
    "quantity": 10
    }
    response = client.post("/tasks", json=retrieve_payload)
    assert response.status_code == 202
    expected = {
        "task_id": "T-001",
        "type": "retrieve",
        "ndc": "NDC_0001",
        "quantity": 10,
        "status": "accepted"
    }
    assert response.json() == expected

def test_create_retrieve_task_quantity_zero():
    bad_payload = {
        "task_id": "T-002",
        "type": "stow",
        "ndc": "NDC_0009",
        "quantity": 0,
    }
    response = client.post("/tasks", json=bad_payload)
    assert response.status_code == 422







