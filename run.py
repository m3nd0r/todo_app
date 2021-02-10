from flask import Flask, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from lib.database import db
from config import Config
from todo import create_app

app = create_app(Config)

Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run(host='localhost', port=5005):
    app.run(host=host, port=port)

if __name__ == '__main__':
    manager.run()
