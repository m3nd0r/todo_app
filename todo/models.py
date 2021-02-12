from flask_login import UserMixin
from sqlalchemy import Binary, Column, Date, DateTime, Integer, String, Text
from werkzeug.security import check_password_hash, generate_password_hash

from todo.mixin import CardMixin, ProjectUserMixin
from todo import login_manager, db


class Card(db.Model):

    __tablename__ = 'Card'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    d_create = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True, index=True)
    status = db.Column(db.String(60), index=True, default='draft')

    def __str__(self):
        return f'<Card {self.id}>' or '---'


class User(UserMixin, db.Model):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    active = db.Column(db.Boolean, default=True)
    d_create = db.Column(db.DateTime(timezone=True))

    def set_password(self, password):
        """ Установить пароль """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Проверить пароль на правильность. """
        if not self.password:
            return False
        return check_password_hash(self.password, password)

    def __str__(self):
        return f'<User {self.id} {self.email}>' or '---'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
