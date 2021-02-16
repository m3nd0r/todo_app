import wtforms
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class AddTodoForm(FlaskForm):
    """
    Форма добавления новой задачи
    """
    todo_content = wtforms.StringField('Название задачи', validators=[validators.Required(message=('Это обязательное поле'))],
                              render_kw={'placeholder': 'Что нужно сделать?'})
    submit = wtforms.SubmitField('Добавить')


class UpdateTodoForm(FlaskForm):
    """
    Форма обновления/модификации задачи
    """
    todo_content = wtforms.StringField('Название задачи', validators=[validators.Required(message=('Это обязательное поле'))],
                              render_kw={'placeholder': 'Что нужно сделать?'})
    submit = wtforms.SubmitField('Изменить')