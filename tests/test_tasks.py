from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

retrieve_payload = {
    "task_id": "T-001",
    "type": "retrieve",
    "ndc": "NDC_0001",
    "quantity": 10
}

def test_create_retrieve_task_happy_path():
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




