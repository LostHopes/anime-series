from tests import client


def test_get_all_anime():
    response = client.get("/anime")
    assert response.status_code == 200
    assert response.json() == {"anime": "Jojo"}

