from flask.views import View
from flask import redirect, request


class AbstractView(View):
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