from dataclasses import dataclass
from eat_it.repesitories import UserRepository

@dataclass
class GetUsersRequest:
    pass

@dataclass
class AddUserRequest:
    user: dict


@dataclass
class PutUserRequest:
    user: dict


@dataclass
class DeleteUserRequest:
    user_id: int


@dataclass 
class PatchUserRequest:
    user: dict


class GetUserController:
    def __init__(self, repository: UserRepository):
        pass

    def get(self, request: GetUsersRequest) -> None:
        raise NotImplementedError()


class AddUserController:
    def __init__(self, repository: UserRepository):
        pass

    def add(self, request: AddUserRequest) -> None:
        raise NotImplementedError()


class PutUserController:
    def __init__(self, repository: UserRepository):
        pass

    def put(self, request: PutUserRequest) -> None:
        raise NotImplementedError


class DeleteUserController:
    def __init__(self, repository: UserRepository):
        pass

    def delete(self, request: DeleteUserRequest) -> None:
        raise NotImplementedError()


class PatchUserController:
    def __init__(self, repository: UserRepository):
        pass

    def patch(self, request: PatchUserRequest) -> None:
        raise NotImplementedError()