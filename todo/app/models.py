from sqlalchemy import Column, DateTime, Integer, String, Text

from todo import db


class Todo(db.Model):

    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    d_create = db.Column(db.DateTime(timezone=True))
    d_modify = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, default=True, index=True)
    status = db.Column(db.String(60), index=True, default='draft')
    user_id = db.Column(db.Integer, db.ForeignKey('todo_user.id'))
    todo_card_id = db.Column(db.Integer, db.ForeignKey('todo_card.id'))

    def __str__(self):
        return f'<Todo {self.id}>' or '---'


class TodoCard(db.Model):

    __tablename__ = 'todo_card'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    active = db.Column(db.Boolean, default=True, index=True)
    status = db.Column(db.String(60), index=True, default='draft')
    todo = db.relationship('Todo', backref='todo_card', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('todo_user.id'))

    @property
    def items(self):
        return Todo.query.filter(Todo.todo_card_id == self.id).all()

    @property
    def sorted_items(self):
        todo_list = Todo.query.filter(Todo.todo_card_id == self.id)
        completed_todos = todo_list.filter_by(status='complete').order_by(Todo.d_modify).all()
        draft_todos = todo_list.filter_by(status='draft').order_by(Todo.d_create).all()

        return draft_todos + completed_todos
