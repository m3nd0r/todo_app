import wtforms
from wtforms import validators
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    """
    Форма логина
    """

    email = wtforms.TextField('Email', validators=[validators.Required(message=('Это обязательное поле')),
                                                   validators.Email(message=('Неверный адрес email'))],
                              render_kw={'placeholder': 'Адрес электронной почты'})
    password = wtforms.PasswordField('Пароль', validators=[validators.Required(message=('Это обязательное поле'))], render_kw={'placeholder': ('Пароль')})