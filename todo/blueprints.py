from flask import Blueprint

from todo import views

blueprint = Blueprint(
    'todo',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/', view_func=views.IndexView.as_view('index'))

blueprint.add_url_rule('/login', view_func=views.LoginView.as_view('login'))
blueprint.add_url_rule('/register', view_func=views.RegistrationView.as_view('register'))

blueprint.add_url_rule('/card', view_func=views.CardView.as_view('card'))

blueprint.add_url_rule('/profile', view_func=views.ProfileView.as_view('profile'))
blueprint.add_url_rule('/character', view_func=views.CharacterView.as_view('character'))
