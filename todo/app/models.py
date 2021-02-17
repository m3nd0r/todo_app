from sqlalchemy import Binary, Column, Date, DateTime, Integer, String, Text

from todo import db
from todo.app.mixin import CardMixin


class TodoCard(db.Model):

    __tablename__ = 'todo_card'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    d_create = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True, index=True)
    status = db.Column(db.String(60), index=True, default='draft')

    def __str__(self):
        return f'<TodoCard {self.id}>' or '---'


class CardPage(db.Model):

    __tablename__ = 'todo_card_page'

    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, db.ForeignKey('todo_card.id'))
