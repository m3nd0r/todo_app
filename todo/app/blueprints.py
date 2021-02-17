from flask import Blueprint

from todo.app import views

from todo.lib.utils import get_todo, user_required

blueprint = Blueprint(
    'todo',
    __name__,
    template_folder='templates',
    static_folder='static'
)

blueprint.add_url_rule('/', view_func=views.IndexView.as_view('index'))

blueprint.add_url_rule('/card', view_func=user_required(views.CardView.as_view('card')))

blueprint.add_url_rule('/add_card', view_func=user_required(views.AddTodoCardView.as_view('add_card')))
blueprint.add_url_rule('/add_todo', view_func=user_required(views.AddTodoView.as_view('add_todo')))

blueprint.add_url_rule('/complete/<int:todo_id>', view_func=views.CompleteTodoView.as_view('complete'))
blueprint.add_url_rule('/delete/<int:todo_id>', view_func=views.DeleteTodoView.as_view('delete'))
blueprint.add_url_rule('/update/<int:todo_id>', view_func=views.ModifyTodoView.as_view('update'))

blueprint.add_url_rule('/profile', view_func=views.ProfileView.as_view('profile'))
blueprint.add_url_rule('/character', view_func=views.CharacterView.as_view('character'))
