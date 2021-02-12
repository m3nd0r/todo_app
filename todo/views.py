from flask import flash, redirect, render_template, url_for
from flask_login import login_user, current_user

from lib.core_views import AbstractView, CoreView
from werkzeug.utils import cached_property

from todo.forms import LoginForm, RegistrationForm


class IndexView(CoreView, AbstractView):

    def get(self):
        return render_template('/index.html')


class CardView(CoreView, AbstractView):

    def get(self):
        return render_template('/card.html')


class ProfileView(CoreView, AbstractView):
    def get(self):
        return render_template('/profile.html')


class CharacterView(CoreView, AbstractView):
    def get(self):
        return render_template('/character.html')


class LoginView(CoreView, AbstractView):

    @cached_property
    def form(self):
        """ Экземпляр формы входа """
        return LoginForm()

    def get(self):
        """ Покажем форму. """
        return render_template('auth/login.html', form=self.form)

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('todo.index'))

        form = self.form
        if form.validate_on_submit():
            data = form.data

            if not current_user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('todo.login'))

            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('todo.index')
                flash('Invalid username or password')
            return redirect(next_page)

        return self.get()


class RegistrationView(CoreView, AbstractView):

    @cached_property
    def form(self):
        """ Экземпляр формы входа """
        return RegistrationForm()

    def get(self):
        """ Покажем форму. """
        return render_template('auth/register.html', form=self.form)

    def register(self):
        if current_user.is_authenticated:
            return redirect(url_for('todo.index'))

        form = self.form
        if form.validate_on_submit():
            user = User(email=form.email.data)
            user.set_password(form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Спасибо за регистрацию!')

            return redirect(url_for('todo.login'))

        return self.get()