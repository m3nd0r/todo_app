from flask import redirect, render_template, url_for
from todo.models import Todo
from lib.core_views import AbstractView


class IndexView(AbstractView):

    def get(self):
        return render_template('/index.html')


class CardView(AbstractView):

    def get(self):
        return render_template('/card.html')
