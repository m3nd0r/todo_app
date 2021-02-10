from os import path

from flask import Blueprint, Flask
from lib.database import db
from todo.blueprints import blueprint


def register_blueprints(app):
    app.register_blueprint(blueprint)

def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

def create_app(config):
    app = Flask(__name__, static_folder='todo/static', template_folder='todo/templates')
    app.config.from_object(config)
    register_blueprints(app)
    configure_database(app)
    db.init_app(app)

    return app
