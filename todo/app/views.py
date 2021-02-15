from flask import flash, redirect, render_template, session, url_for, request
from todo.lib.core_views import AbstractView, CoreView
from todo.app.models import Card
from todo.app.forms import AddTodoForm
from todo import db
from datetime import datetime
from werkzeug.utils import cached_property
from flask.views import MethodView


class IndexView(CoreView, MethodView):

    def get(self):
        return render_template('/index.html')


class CardView(CoreView, MethodView):

    @cached_property
    def form(self):
        """ Экземпляр формы добавления новой задачи """
        return AddTodoForm()

    def get(self):
        todo_list = Card.query.all()
        return render_template('/card.html', form = self.form, todo_list=todo_list)

    def post(self):
        form = self.form

        if form.validate_on_submit():
            new_todo = Card(content=form.todo_content.data, d_create=datetime.now())
            db.session.add(new_todo)
            db.session.commit()

            return redirect(url_for('todo.card'))


class DeleteTodoView(CoreView, MethodView):

    def get(self, todo_id):
        print(todo_id)
        todo = Card.query.filter_by(id=todo_id).first()
        db.session.delete(todo)
        db.session.commit()

        return redirect(url_for('todo.card'))


class ProfileView(CoreView, MethodView):
    def get(self):
        return render_template('/profile.html')


class CharacterView(CoreView, MethodView):
    def get(self):
        return render_template('/character.html')
