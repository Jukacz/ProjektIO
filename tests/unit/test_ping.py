from eat_it.app import ping, users_get, users_post, users_put, users_delete, app, users_patch

UNIMPLEMENTED = 501
OK = 200
# code 204


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED


def tese_users_get_returns_501_response() -> None:
    result = users_get()
    assert result.status_code == UNIMPLEMENTED


def test_create_user_returns_user() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = users_post()
    assert result.json == payload and result.status_code == 201


def test_users_put_returns_id() -> None:
    payload = {"id": 1}
    with app.test_request_context(method="PUT", path="/users_put", json=payload):
        result = users_put()
    assert result.json == payload and result.status_code == OK


def test_users_patch_returns_id() -> None:
    payload = {"id": 1}
    with app.test_request_context(method="PATCH", path="/users_patch", json=payload):
        result = users_patch()
    assert result.json == payload and result.status_code == OK


def test_users_delete_returns_id() -> None:
    payload = 2
    with app.test_request_context(method="DELETE", path=f"/users_delete/{payload}"):
        result = users_delete(payload)
    assert result.status_code == 204