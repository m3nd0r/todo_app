from flask.views import View
from flask import redirect, request, g

# from lib.utils import get_current_user


class AbstractView(View):
    """
    Приместь ко всем вьюхам
    """
    methods = ['GET', 'POST']

    def dispatch_request(self, **kwargs):
        response = getattr(self, request.method.lower())()

        return response

    def get(self):
        return redirect('/')

    def head(self):
        return redirect('/')

    def post(self):
        return redirect('/')


class CoreView(object):
    """
    Всякие разные постоянно повторяющиеся методы и утилки
    """
    pass