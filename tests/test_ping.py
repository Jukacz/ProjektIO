from eat_it.app import UserView, UserAddView, UserPutView, UserPatchView, UserDeleteView, app
from eat_it.app import GetUserController, AddUserController, PutUserController, PatchUserController, DeleteUserController

UNIMPLEMENTED = 501
OK = 200
# code 204


def tese_users_get_returns_501_response() -> None:
    result = UserView(controller=GetUserController()).get()
    assert result.status_code == UNIMPLEMENTED


def test_create_user_returns_user():
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    with app.test_request_context(method="POST", path="/users_post", json=payload):
        result = UserAddView(controller=AddUserController()).post()
    assert result.status_code == 201


def test_users_put_returns_id() -> None:
    payload = {"id": 1}
    id = 1
    with app.test_request_context(method="PUT", path=f"/users_put/{id}", json=payload):
        result = UserPutView(controller=PutUserController()).put(id=id)
    assert result.json == payload and result.status_code == OK


def test_users_patch_returns_id() -> None:
    payload = {"id": 1}
    id = 1
    with app.test_request_context(method="PATCH", path=f'/users_patch/{id}', json=payload):
        result = UserPatchView(controller=PatchUserController()).patch(id=id)
    assert result.json == payload and result.status_code == OK


def test_users_delete_returns_id() -> None:
    id = 2
    with app.test_request_context(method="DELETE", path=f"/users_delete/{id}"):
        result = UserDeleteView(
            controller=DeleteUserController()).delete(id=id)
    assert result.status_code == 204
