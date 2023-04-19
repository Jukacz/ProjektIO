from flask import Response, jsonify, request
from flask.views import MethodView
from eat_it.controllers import GetUsersRequest, AddUserRequest, PatchUserRequest, PutUserRequest, DeleteUserRequest
from eat_it.controllers import GetUserController, AddUserController, PutUserController, PatchUserController, DeleteUserController


class UserView(MethodView):
    def __init__(self, controller: GetUserController) -> None:
        self.controller = controller
        pass

    def get(self) -> Response:
        try:
            add_user_request = GetUsersRequest()
            self.controller.get(request=add_user_request)
        except NotImplementedError:
            pass
        return Response(status=501)


class UserAddView(MethodView):
    def __init__(self, controller: AddUserController) -> None:
        self.controller = controller
        pass

    def post(self) -> Response:
        try:
            user = request.json
            add_user_request = AddUserRequest(user=user)
            self.controller.add(request=add_user_request)
        except NotImplementedError:
            pass
        return Response(status=201, response=user)


class UserPutView(MethodView):
    def __init__(self, controller: PutUserController) -> None:
        self.controller = controller
        pass

    def put(self, id) -> Response:
        try:
            user = request.json
            patch_user_request = PutUserRequest(user=request.json)
            self.controller.put(request=patch_user_request)
        except NotImplementedError:
            pass
        return jsonify(user)


class UserPatchView(MethodView):
    def __init__(self, controller: PatchUserController) -> None:
        self.controller = controller
        pass

    def patch(self, id) -> Response:
        try:
            user = request.json
            patch_user_request = PatchUserRequest(user=user)
            self.controller.patch(request=patch_user_request)
        except NotImplementedError:
            pass
        return jsonify(user)


class UserDeleteView(MethodView):
    def __init__(self, controller: DeleteUserController) -> None:
        self.controller = controller
        pass

    def delete(self, id) -> Response:
        try:
            delete_user_request = DeleteUserRequest(user_id=id)
            self.controller.delete(request=delete_user_request)
        except NotImplementedError:
            pass
        return Response(status=204)
