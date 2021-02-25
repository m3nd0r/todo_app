from os import path

from flask import Blueprint, Flask
from flask_login import LoginManager, current_user
from todo.lib.database import db
from todo.app.blueprints import blueprint as bp1
from todo.auth.blueprints import blueprint as bp2
from todo.char.blueprints import blueprint as bp3

from todo.config import Config
from flask_script import Manager

app = Flask(
    __name__,
    static_url_path='',
    static_folder='lib/static')
app.config.from_object(Config)

app.register_blueprint(bp1)
app.register_blueprint(bp2)
app.register_blueprint(bp3)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.blueprint_login_views = 'todo.auth.login'

from todo.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
