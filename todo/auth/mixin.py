from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import cached_property
from todo.char.models import Character, Race, Gender, Profession

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


class CharacterMixin():
    """
    Вынесу сюда всё, связанное с персонажем
    """
    @cached_property
    def character(self):
        return Character.query.filter_by(user_id=self.id).first()

    @cached_property
    def race(self):
        return Race.query.filter_by(id=self.character.race_id).first()

    @cached_property
    def profession(self):
        return Profession.query.filter_by(id=self.character.profession_id).first()

    @cached_property
    def gender(self):
        return Gender.query.filter_by(id=self.character.gender_id).first()
