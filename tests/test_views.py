from eat_it.views import UserView, UserAddView, UserPutView, UserPatchView, UserDeleteView
from eat_it.controllers import GetUserController, AddUserController, PutUserController, PatchUserController, DeleteUserController
from unittest.mock import Mock
from flask import Response
import pytest


# Mocks for controllers
@pytest.fixture
def getController() -> Mock:
    return Mock(GetUserController)


@pytest.fixture
def addController() -> Mock:
    return Mock(AddUserController)


@pytest.fixture
def putController() -> Mock:
    return Mock(PutUserController)


@pytest.fixture
def patchController() -> Mock:
    return Mock(PatchUserController)


@pytest.fixture
def deleteController() -> Mock:
    return Mock(DeleteUserController)


# fixture for views


@pytest.fixture
def getView(getController: GetUserController) -> UserView:
    return UserView(controller=getController)


@pytest.fixture
def addView(addController: AddUserController) -> UserAddView:
    return UserAddView(controller=addController)


@pytest.fixture
def putView(putController: PutUserController) -> UserPutView:
    return UserPutView(controller=putController)


@pytest.fixture
def patchView(patchController: PatchUserController) -> UserPatchView:
    return UserPatchView(controller=patchController)


@pytest.fixture
def deleteView(deleteController: DeleteUserController) -> UserDeleteView:
    return UserDeleteView(controller=deleteController)


# tests


def test_user_view_return_response_on_get_method(getView: UserView) -> None:
    result = getView.get()
    assert isinstance(result, Response)


def test_user_view_returns_501_response(getView: UserView) -> None:
    result = getView.get()
    assert result.status_code == 501


def test_user_view_is_subclasS_method_view(getView: UserView) -> None:
    assert isinstance(getView, UserView)


def test_user_post_view_return_response_on_post_method(addView: UserAddView) -> None:
    result = addView.post()
    assert isinstance(result, Response)


def test_user_add_view_returns_501_response(addView: UserAddView) -> None:
    result = addView.post()
    assert result.status_code == 501


def test_user_post_view_is_subclasS_method_view(addView: UserAddView) -> None:
    assert isinstance(addView, UserAddView)


def test_user_put_view_return_response_on_put_method(putView: UserPutView) -> None:
    result = putView.put()
    assert isinstance(result, Response)


def test_user_put_view_returns_501_response(putView: UserPutView) -> None:
    result = putView.put()
    assert result.status_code == 501


def test_user_put_view_is_subclasS_method_view(putView: UserPutView) -> None:
    assert isinstance(putView, UserPutView)


def test_user_patch_view_return_response_on_patch_method(patchView: UserPatchView) -> None:
    result = patchView.patch()
    assert isinstance(result, Response)


def test_user_patch_view_returns_501_response(patchView: UserPatchView) -> None:
    result = patchView.patch()
    assert result.status_code == 501


def test_user_patch_view_is_subclasS_method_view(patchView: UserPatchView) -> None:
    assert isinstance(patchView, UserPatchView)


def test_user_delete_view_return_response_on_delete_method(deleteView: UserDeleteView) -> None:
    result = deleteView.delete()
    assert isinstance(result, Response)


def test_user_delete_view_returns_501_response(deleteView: UserDeleteView) -> None:
    result = deleteView.delete()
    assert result.status_code == 501


def test_user_delete_view_is_subclasS_method_view(deleteView: UserDeleteView) -> None:
    assert isinstance(deleteView, UserDeleteView)
