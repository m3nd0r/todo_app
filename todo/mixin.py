from flask_login import UserMixin


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
    pass
