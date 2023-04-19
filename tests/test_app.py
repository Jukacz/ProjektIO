from eat_it.app import app

UNIMPLEMENTED = 501


def test_app_has_users_get_endpoint() -> None:
    client = app.test_client()
    response = client.get(path="/users_get")
    assert response.status_code == UNIMPLEMENTED


def test_app_has_users_post_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users_post', json=payload)
    assert response.status_code == 201


def test_app_has_users_put_endpoint() -> None:
    payload = {"id": 1}
    client = app.test_client()
    response = client.put(path="/users_put/1", json=payload)
    assert response.json == payload and response.status_code == 200


def test_app_has_users_patch_endpoint() -> None:
    payload = {"id": 1}
    client = app.test_client()
    response = client.patch(path="/users_patch/1", json=payload)
    assert response.status_code == 200


def test_app_has_users_delete_endpoint() -> None:
    client = app.test_client()
    response = client.delete(path="/users_delete/2")
    assert response.status_code == 204
