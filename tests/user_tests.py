import json

import pytest

from eat_it.app import app
from eat_it.app import users_post
from eat_it.app import users_patch


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


def test_users_post_returns_user(payload: dict) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = users_post()
    assert result.json == payload


def test_users_post_prints_user_on_console(payload: dict, capsys) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        users_post()
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_update_user_returns_user(payload: dict) -> None:
    with app.test_request_context(method="PUT", path="/users", json=payload):
        result = users_patch()
    assert result.json == payload
