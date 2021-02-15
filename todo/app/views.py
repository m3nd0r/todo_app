from flask import flash, redirect, render_template, session, url_for
from todo.lib.core_views import AbstractView, CoreView


class IndexView(CoreView, AbstractView):

    def get(self):
        return render_template('/index.html')


class CardView(CoreView, AbstractView):

    def get(self):
        return render_template('/card.html')


class ProfileView(CoreView, AbstractView):
    def get(self):
        return render_template('/profile.html')


class CharacterView(CoreView, AbstractView):
    def get(self):
        return render_template('/character.html')
