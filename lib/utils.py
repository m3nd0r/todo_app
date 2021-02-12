
# from flask import g
# from todo.models import User

# def get_current_user(default_email=None):
#     """
#     Получить текущего оператора.
#     Если его нет, вернуть оператора с email == default_email
#     """
#     user = getattr(g, 'user', None)
#     if user and user.is_authenticated:
#         return user

#     if default_email:
#         return User.query.filter_by(email=default_email).first()