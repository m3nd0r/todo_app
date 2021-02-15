from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class CardMixin():
    pass


class ProjectUserMixin(UserMixin):
    """
    Здесь описывается вся логика пользователя:
    - смена и проверка паролей
    - проверка онлайн или нет
    - логаут
    - какие-нибудь уведомления
    """


    def check_password(self, password):
        """ Проверить пароль на правильность. """
        if not self.password:
            return False
        return check_password_hash(self.password, password)

    def set_password(self, password):
        """ Установить пароль """
        self.password = generate_password_hash(password)

    def validate_email(self, email):
        cls = self.__class__

        email = cls.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Такой e-mail уже зарегистрирован.')