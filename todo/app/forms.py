import wtforms
from wtforms import validators
from flask_wtf import FlaskForm
from todo.app.models import Todo


class AddTodoCardForm(FlaskForm):
    """
    Форма добавления новой задачи
    """
    todo_card_name = wtforms.StringField('Название карточки', validators=[validators.Required(message=('Это обязательное поле'))])
    submit = wtforms.SubmitField('Создать')


class AddTodoForm(FlaskForm):
    """
    Форма добавления новой задачи
    """
    todo_content = wtforms.StringField('Название задачи', validators=[validators.Required(message=('Это обязательное поле'))],
                              render_kw={'placeholder': 'Что нужно сделать?'})
    todo_card_id = wtforms.HiddenField()
    submit = wtforms.SubmitField('Добавить')


class UpdateTodoForm(FlaskForm):
    """
    Форма обновления/модификации задачи
    """
    todo_content = wtforms.StringField('Название задачи', validators=[validators.Required(message=('Это обязательное поле'))],
                              render_kw={'placeholder': 'Что нужно сделать?'})
    submit = wtforms.SubmitField('Изменить')