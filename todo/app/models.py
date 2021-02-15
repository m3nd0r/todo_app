from sqlalchemy import Binary, Column, Date, DateTime, Integer, String, Text
from werkzeug.security import generate_password_hash

from todo import db
from todo.app.mixin import CardMixin


class Card(db.Model):

    __tablename__ = 'Card'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    d_create = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True, index=True)
    status = db.Column(db.String(60), index=True, default='draft')

    def __str__(self):
        return f'<Card {self.id}>' or '---'
