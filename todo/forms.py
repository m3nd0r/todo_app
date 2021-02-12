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
    submit = wtforms.SubmitField('Войти')


class RegistrationForm(FlaskForm):
    """
    Форма регистрации
    """
    email = wtforms.TextField('Email', validators=[validators.Email(message=('Неверный адрес email'))],
                              render_kw={'placeholder': 'Адрес электронной почты'})
    password = wtforms.PasswordField('Пароль', validators=[validators.DataRequired()])
    password2 = wtforms.PasswordField('Пароль повторно', validators=[validators.DataRequired(), validators.EqualTo('password')])
    submit = wtforms.SubmitField('Зарегистрироваться')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Такой e-mail уже зарегистрирован.')