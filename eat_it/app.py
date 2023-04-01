from flask import Flask, Response, request, jsonify
from repesitories import UserRepository
from controllers import AddUserController, GetUserController, AddUserRequest, GetUsersRequest, PutUserController, PutUserRequest, PatchUserController, PatchUserRequest, DeleteUserController, DeleteUserRequest
app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.get("/users_get")
def users_get() -> Response:
    repesitory = UserRepository()
    controller = GetUserController(repesitory=repesitory)
    try:
        add_user_request = GetUsersRequest()
        controller.get(request=add_user_request)
    except NotImplementedError:
        pass
    return Response(status=501)


@app.post("/users_post")
def users_post() -> Response:
    user = request.json
    repesitory = UserRepository()
    controller = AddUserController(repesitory=repesitory)
    try:
        add_user_request = AddUserRequest(user=user)
        controller.add(request=add_user_request)
    except NotImplementedError:
        pass
    return Response(status=201, response=user)


@app.put("/users_put/<id>")
def users_put(id) -> Response:
    user = request.json
    repesitory = UserRepository()
    controller = PutUserController(repesitory=repesitory)

    try:
        put_user_request = PutUserRequest(user=user)
        controller.put(request=put_user_request)
    except NotImplementedError:
        pass
    return jsonify(user)


@app.patch("/users_patch/<id>")
def users_patch(id) -> Response:
    user = request.json
    repesitory = UserRepository()
    controller = PatchUserController(repesitory=repesitory)
    try:
        patch_user_request = PatchUserRequest(user=request.json)
        controller.patch(request=patch_user_request)
    except NotImplementedError:
        pass
    return jsonify(user)


@app.delete("/users_delete/<id>")
def users_delete(id) -> Response:
    repesitory = UserRepository()
    controller = DeleteUserController(repesitory=repesitory)
    try:
        delete_user_request = DeleteUserRequest(id=id)
        controller.delete(request=delete_user_request)
    except NotImplementedError:
        pass

    return Response(status=204)
