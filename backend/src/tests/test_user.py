from tests import client


def test_get_all_users():
    response = client.get("/users/49i558user")
    assert response.status_code == 200