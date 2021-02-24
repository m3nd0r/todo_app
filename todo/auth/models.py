from .mixin import ProjectUserMixin, CharacterMixin
from todo import db


class User(ProjectUserMixin, CharacterMixin, db.Model):

    __tablename__ = 'todo_user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    active = db.Column(db.Boolean, default=True)
    d_create = db.Column(db.DateTime(timezone=True))

    todo_card = db.relationship('TodoCard', backref='user', lazy='dynamic')
    todo = db.relationship('Todo', backref='user', lazy='dynamic')
    character_id = db.Column(db.Integer, db.ForeignKey('todo_character.id'))

    def __str__(self):
        return f'<User {self.id} {self.email}>' or '---'
