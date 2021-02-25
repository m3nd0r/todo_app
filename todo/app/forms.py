import wtforms
from flask_wtf import FlaskForm
from todo.app.models import Todo
from wtforms import validators
from wtforms_sqlalchemy.fields import QuerySelectField


class AddTodoCardForm(FlaskForm):
    """
    Форма добавления новой карточки
    """
    todo_card_name = wtforms.StringField('Название карточки', validators=[validators.Required(message=('Это обязательное поле'))],
                                render_kw={
                                    'placeholder': 'Название карточки',
                                    'id': 'button-addon2',
                                    'aria-describedby': 'button-addon2',
                                })
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
                              render_kw={
                                  'placeholder': 'Новое значение',
                                  'aria-describedby': 'button-addon2',
                                  })
    todo_card_id = wtforms.HiddenField()
    submit = wtforms.SubmitField('Изменить', render_kw={'id': 'button-addon2'})


class RenameCardForm(FlaskForm):
    """
    Форма переименования карточки
    """
    todo_content = wtforms.StringField('Новое название', validators=[validators.Required(message=('Это обязательное поле'))],
                              render_kw={
                                  'placeholder': 'Новое название',
                                  'aria-describedby': 'button-addon2',
                                  })
    todo_card_id = wtforms.HiddenField()
    submit = wtforms.SubmitField('Изменить', render_kw={'id': 'button-addon2'})
