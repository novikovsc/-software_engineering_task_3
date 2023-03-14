from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/day/1")
    assert response.status_code == 200
    assert response.json() == {"day": "monday"}

    response = client.get("/day/2")
    assert response.status_code == 200
    assert response.json() == {"day": "tuesday"}

    response = client.post("/all")
    assert response.status_code == 200
    assert response.json() == {"1": "monday", "2": "tuesday", "3": "wednesday", "4": "thursday", "5": "friday",
                               "6": "saturday", "7": "sunday"}