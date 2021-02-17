from .mixin import ProjectUserMixin
from todo import db


class User(ProjectUserMixin, db.Model):

    __tablename__ = 'todo_user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    active = db.Column(db.Boolean, default=True)
    d_create = db.Column(db.DateTime(timezone=True))
    card = db.relationship('TodoCard', backref='author', lazy='dynamic')

    def __str__(self):
        return f'<User {self.id} {self.email}>' or '---'
