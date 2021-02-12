from os import path

from flask import Blueprint, Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from todo.blueprints import blueprint
from todo.config import Config

app = Flask(__name__, static_folder='todo/static', template_folder='todo/templates')
app.config.from_object(Config)
app.register_blueprint(blueprint)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.blueprint_login_views = 'todo.login'

from todo import views, models