from flask import redirect, render_template, url_for
from todo.models import Todo

def index():
    first_todo = Todo.query.filter_by(id=1).first()
    return render_template('/index.html', first_todo=first_todo)
