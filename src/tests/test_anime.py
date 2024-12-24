from fastapi.testclient import TestClient
from anime import app


client = TestClient(app)


def test_get_all_anime():
    response = client.get("/anime")
    assert response.status_code == 200
    assert response.json() == {"anime": "Jojo"}

