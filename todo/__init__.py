from os import path

from flask import Blueprint, Flask
from flask_login import LoginManager
from todo.lib.database import db
from todo.app.blueprints import blueprint as bp1
from todo.auth.blueprints import blueprint as bp2
from todo.config import Config
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(bp1)
app.register_blueprint(bp2)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.blueprint_login_views = 'todo.auth.login'

from todo.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))