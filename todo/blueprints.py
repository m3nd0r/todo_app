from flask import Blueprint

from todo import views

blueprint = Blueprint(
    'todo_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/', view_func=views.IndexView.as_view('index'))
blueprint.add_url_rule('/card.html', view_func=views.CardView.as_view('card'))
blueprint.add_url_rule('/login.html', view_func=views.LoginView.as_view('login'))
