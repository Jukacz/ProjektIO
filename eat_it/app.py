from flask import Flask
from .repesitories import UserRepository
from .views import UserView, UserAddView, UserPutView, UserPatchView, UserDeleteView
from .controllers import AddUserController, GetUserController,  PutUserController,  PatchUserController,  DeleteUserController

from views import UserView
app = Flask(__name__)


app.add_url_rule("/users_get", view_func=UserView.as_view("users",
                 controller=GetUserController(repository=UserRepository())))
app.add_url_rule("/users_post", view_func=UserAddView.as_view("users",
                 controller=AddUserController(repository=UserRepository())))
app.add_url_rule("/users_put/<id>", view_func=UserPutView.as_view("users",
                 controller=PutUserController(repository=UserRepository())))
app.add_url_rule("/users_patch/<id>", view_func=UserPatchView.as_view("users",
                 controller=PatchUserController(repository=UserRepository())))
app.add_url_rule("/users_delete/<id>", view_func=UserDeleteView.as_view("users",
                 controller=DeleteUserController(repository=UserRepository())))
