from flask import Blueprint

from todo.auth import views

blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
blueprint.add_url_rule('/logout', view_func=views.LogoutView.as_view('logout'))
blueprint.add_url_rule('/register', view_func=views.RegistrationView.as_view('register'))
