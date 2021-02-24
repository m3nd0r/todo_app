from datetime import datetime

from flask import flash, redirect, render_template, request, session, url_for
from flask.views import MethodView
from flask_login import current_user
from todo import db
from todo.char.forms import CreateCharacterForm
from todo.char.models import Character
from todo.lib.core_views import CoreView
from todo.lib.utils import get_todo, get_todo_card
from werkzeug.utils import cached_property


class CharacterView(CoreView, MethodView):
    """
    Просмотр персонажа пользователя
    """
    def get(self):
        return render_template('/character.html', form=CreateCharacterForm())


class RegistrationView(CoreView, MethodView):

    @cached_property
    def form(self):
        """ Экземпляр формы создания персонажа """
        return CreateCharacterForm()

    def get(self):
        """ Покажем форму. """
        return render_template('character.html', form=self.form)

    def post(self):
        form = self.form
        if form.validate_on_submit():

            character = Character(
                name=form.name.data,
                gender_id=form.gender.data.id,
                race_id=form.race.data.id,
                profession_id=form.profession.data.id,
                user_id=current_user.id,
                d_create=datetime.now()
            )

            db.session.add(character)
            db.session.commit()
            flash('Персонаж создан!')

            return redirect(url_for('char.character'))

        return self.get()