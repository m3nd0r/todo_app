import wtforms
from flask_wtf import FlaskForm
from todo.char.models import Race, Gender, Profession
from wtforms import validators
from wtforms_sqlalchemy.fields import QuerySelectField

def race_query():
    return Race.query

def gender_query():
    return Gender.query

def profession_query():
    return Profession.query


class CreateCharacterForm(FlaskForm):
    """
    Форма создания персонажа
    """
    name = wtforms.StringField('Имя персонажа', validators=[validators.Required(message=('Это обязательное поле'))],
        render_kw={'placeholder': 'Имя персонажа'})
    gender = QuerySelectField(query_factory=gender_query)
    race = QuerySelectField(query_factory=race_query)
    profession = QuerySelectField(query_factory=profession_query)
    submit = wtforms.SubmitField('Создать')
