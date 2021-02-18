
from functools import wraps

from flask import g, redirect, url_for
from flask_login import current_user
from todo.app.models import Todo, TodoCard
from todo.auth.models import User


def get_current_user(default_email=None):
    """
    Получить текущего оператора.
    Если его нет, вернуть оператора с email == default_email
    """
    user = current_user
    if user and user.is_authenticated:
        return user

    if default_email:
        return User.query.filter_by(email=default_email).first()

def get_todo(todo_id):
    """
    Получить объект todo
    """
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        return todo

def get_todo_card(todo_card_id):
    """
    Получить объект todo
    """
    todo_card = TodoCard.query.filter_by(id=todo_card_id).first()
    if todo_card:
        return todo_card

def user_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
            # or, if you're not using Flask-Login
            # return redirect(url_for('login_page'))
        return f(*args, **kwargs)
    return decorator
