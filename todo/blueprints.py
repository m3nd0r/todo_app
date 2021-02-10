from flask import Blueprint
from todo.views import index

blueprint = Blueprint(
    'todo_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule(
    'index',
    view_func=index
)