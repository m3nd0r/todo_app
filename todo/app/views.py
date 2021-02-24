from datetime import datetime

from flask import flash, redirect, render_template, request, session, url_for
from flask.views import MethodView
from flask_login import current_user
from todo import db
from todo.app.forms import AddTodoCardForm, AddTodoForm, UpdateTodoForm
from todo.app.models import Todo, TodoCard
from todo.lib.core_views import AbstractView, CoreView
from todo.lib.utils import get_todo, get_todo_card
from werkzeug.utils import cached_property


class IndexView(CoreView, MethodView):
    """
    Главная страница
    """
    def get(self):
        return render_template('/index.html')


class CardView(CoreView, MethodView):
    """
    Страница с отображением всех карточек
    """
    def get(self):
        add_card_form = AddTodoCardForm()
        add_todo = AddTodoForm()
        update_form = UpdateTodoForm()
        todo_card_list = TodoCard.query.filter_by(user_id=current_user.id).all()
        return render_template(
            '/card.html',
            add_card_form=add_card_form,
            add_todo=add_todo,
            update_form=update_form,
            todo_card_list=todo_card_list)

class ArchiveView(CoreView, MethodView):
    """
    Страница с отображением всех карточек
    """
    def get(self):
        add_todo = AddTodoForm()
        update_form = UpdateTodoForm()
        todo_card_list = TodoCard.query.filter_by(user_id=current_user.id).all()
        return render_template(
            '/archive.html',
            add_todo=add_todo,
            update_form=update_form,
            todo_card_list=todo_card_list)


class AddTodoCardView(CoreView, MethodView):
    """
    Добавление карточки
    """
    @cached_property
    def form(self):
        return AddTodoCardForm()

    def get(self):
        todo_card_list = TodoCard.query.filter_by(user_id=current_user.id).all()
        return render_template('/card.html', add_card_form=self.form, todo_card_list=todo_card_list)

    def post(self):
        form = self.form
        if form.validate_on_submit():
            new_todo_card = TodoCard(
                user_id=current_user.id,
                name=form.todo_card_name.data
            )
            db.session.add(new_todo_card)
            db.session.commit()

            return redirect(url_for('todo.card'))


class AddTodoView(CoreView, MethodView):
    """
    Добавление одной задачи
    """
    @cached_property
    def form(self):
        """ Экземпляр формы добавления новой задачи """
        return AddTodoForm()

    def get(self):
        return redirect(url_for('todo.card'))

    def post(self):
        form = self.form
        if form.validate_on_submit():
            new_todo = Todo(
                content=form.todo_content.data,
                active=True,
                d_create=datetime.now(),
                user_id=current_user.id,
                todo_card_id=form.todo_card_id.data
            )
            db.session.add(new_todo)
            db.session.commit()

            return redirect(url_for('todo.card'))


class DeleteTodoView(CoreView, MethodView):
    """
    Удаление одной задачи
    """
    def get(self, todo_id):
        todo = get_todo(todo_id)
        todo.active = False
        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todo.card'))


class ModifyTodoView(CoreView, MethodView):
    """
    Изменение одной задачи
    """
    @cached_property
    def form(self):
        """ Экземпляр формы модификации задачи """
        return UpdateTodoForm()

    def get(self, todo_id):
        todo = get_todo(todo_id)
        return render_template('/update.html', form=self.form, todo=todo)

    def post(self, todo_id):
        todo = get_todo(todo_id)
        form = self.form
        if form.validate_on_submit():
            todo.content = form.todo_content.data
            db.session.add(todo)
            db.session.commit()

            return redirect(url_for('todo.card'))


class CompleteTodoView(CoreView, MethodView):
    """
    Завершение задачи
    """
    def get(self, todo_id):
        todo = get_todo(todo_id)
        if todo:
            if todo.status == 'draft':
                todo.status = 'complete'
            else:
                todo.status = 'draft'

            db.session.add(todo)
            db.session.commit()
        else:
            flash(f'Задачи №{todo_id} не существует!', 'warning')

        return redirect(url_for('todo.card'))


class DeleteTodoCardView(CoreView, MethodView):
    """
    Удаление одной задачи
    """
    def get(self, todo_card_id):
        todo_card = get_todo_card(todo_card_id)
        todo_card.active = False
        db.session.add(todo_card)
        db.session.commit()

        return redirect(url_for('todo.card'))


class ProfileView(CoreView, MethodView):
    """
    Просмотр профиля пользователя
    """
    def get(self):
        return render_template('/profile.html')
