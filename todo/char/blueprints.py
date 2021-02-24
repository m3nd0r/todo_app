from flask import Blueprint

from todo.char import views

from todo.lib.utils import get_todo, user_required

blueprint = Blueprint(
    'char',
    __name__,
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/create_character', view_func=user_required(views.RegistrationView.as_view('create_character')))

blueprint.add_url_rule('/character', view_func=user_required(views.CharacterView.as_view('character')))
