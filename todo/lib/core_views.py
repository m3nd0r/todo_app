from flask import g, redirect, request
from flask.views import MethodView

from todo.lib.utils import get_current_user


class AbstractView(MethodView):
    """
    Приместь ко всем вьюхам
    """
    methods = ['GET', 'POST', 'DELETE']

    def dispatch_request(self, **kwargs):
        response = getattr(self, request.method.lower())()

        return response

    def get(self):
        return redirect('/')

    def head(self):
        return redirect('/')

    def post(self):
        return redirect('/')

    def delete(self):
        return redirect('/')

    def put(self):
        return redirect('/')


class CoreView(object):
    """
    Всякие разные постоянно повторяющиеся методы и утилки
    """
    @property
    def user(self):
        return get_current_user()
