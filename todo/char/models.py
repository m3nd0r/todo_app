from sqlalchemy import Column, DateTime, Integer, String, Text

from todo import db


class Character(db.Model):
    """Модель персонажа"""
    __tablename__ = 'todo_character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True)
    gender_id = db.Column(db.Integer, db.ForeignKey('todo_gender.id'))
    race_id = db.Column(db.Integer, db.ForeignKey('todo_race.id'))
    profession_id = db.Column(db.Integer, db.ForeignKey('todo_profession.id'))
    d_create = db.Column(db.DateTime(timezone=True))

    user_id = db.Column(db.Integer, db.ForeignKey('todo_user.id'))

    def __str__(self):
        return f'Character {self.id} {self.name}'


class Gender(db.Model):
    """Модель пола"""
    __tablename__ = 'todo_gender'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)

    def __str__(self):
        return f'Gender {self.gender}'


class Race(db.Model):
    """Модель рассы"""
    __tablename__ = 'todo_race'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    extra = db.Column(db.Text, index=True)

    def __str__(self):
        return f'Race {self.id} {self.name}'


class Profession(db.Model):
    """Модель класса персонажа"""
    __tablename__ = 'todo_profession'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True)
    extra = db.Column(db.Text, index=True)

    def __str__(self):
        return f'Profession {self.id} {self.name}'
