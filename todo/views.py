from flask import redirect, render_template, url_for, flash
from lib.core_views import AbstractView
from werkzeug.utils import cached_property
from flask_login import login_user
from todo.forms import LoginForm
from todo.models import Todo


class IndexView(AbstractView):

    def get(self):
        return render_template('/index.html')


class CardView(AbstractView):

    def get(self):
        return render_template('/card.html')


class LoginView(AbstractView):

    @cached_property
    def form(self):
        """ Экземпляр формы входа """
        return LoginForm()

    def get(self):
        """ Покажем форму. """
        return render_template('auth/login.html', form=self.form)

    def login(self):

        if current_user.is_authenticated:
            return redirect(url_for('todo_blueprint.index'))

        form = self.form
        if form.validate_on_submit():
            data = form.data
            user = User.query.filter_by(username=form.username.data).first()

            if not user or not user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('todo_blueprint.login'))

            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('todo_blueprint.index')
            return redirect(next_page)

        return self.get()