from flask_login import UserMixin
from lib.database import db
from sqlalchemy import Binary, Column, Date, DateTime, Integer, String, Text
from werkzeug.security import generate_password_hash, check_password_hash
from todo.mixin import CardMixin, ProjectUserMixin


class Todo(db.Model):

    __tablename__ = 'Todo'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)

    def __str__(self):
        return f'{self.id} {self.content}'


class Card(CardMixin, db.Model):

    __tablename__ = 'Card'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    d_create = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True, index=True)
    status = db.Column(db.String(60), index=True, default='draft')


    def __str__(self):
        return f'<Card {self.id}>' or '---'


class User(ProjectUserMixin, UserMixin, db.Model):

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