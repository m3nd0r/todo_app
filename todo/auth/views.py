from flask import flash, redirect, render_template, session, url_for, request
from flask_login import current_user, login_user, logout_user
from todo import db
from todo.lib.core_views import AbstractView, CoreView
from werkzeug.utils import cached_property
from datetime import datetime
from .forms import LoginForm, RegistrationForm
from .models import User
from flask.views import MethodView


class LoginView(CoreView, MethodView):

    @cached_property
    def form(self):
        """ Экземпляр формы входа """
        return LoginForm()

    def get(self):
        """ Покажем форму. """
        return render_template('/login.html', form=self.form)

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('todo.index'))
        else:
            form = self.form
            if form.validate_on_submit():
                data = form.data
                user = User.query.filter_by(email=form.email.data).first()
                if not user or not user.check_password(form.password.data):
                    flash('Неверный email или пароль')
                    return redirect(url_for('auth.login'))

                login_user(user)
                next_page = request.args.get('next')

                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('todo.index')

                return redirect(next_page)


class RegistrationView(CoreView, MethodView):

    @cached_property
    def form(self):
        """ Экземпляр формы регистрации """
        return RegistrationForm()

    def get(self):
        """ Покажем форму. """
        return render_template('register.html', form=self.form)

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('todo.index'))

        form = self.form
        if form.validate_on_submit():

            user = User(email=form.email.data, d_create=datetime.now())
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Спасибо за регистрацию!')

            return redirect(url_for('auth.login'))

        return self.get()


class LogoutView(CoreView, MethodView):
    """ Выйти из системы. """

    def get(self):
        logout_user()

        return redirect(url_for('todo.index'))