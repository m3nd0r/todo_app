from lib.database import db
from sqlalchemy import Binary, Column, Date, Integer, String, Text


class Todo(db.Model):

    __tablename__ = 'Todo'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.content}'
