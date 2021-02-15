from flask import Blueprint

from todo.app import views

blueprint = Blueprint(
    'todo',
    __name__,
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/', view_func=views.IndexView.as_view('index'))

blueprint.add_url_rule('/card', view_func=views.CardView.as_view('card'))
blueprint.add_url_rule('/profile', view_func=views.ProfileView.as_view('profile'))
blueprint.add_url_rule('/character', view_func=views.CharacterView.as_view('character'))
