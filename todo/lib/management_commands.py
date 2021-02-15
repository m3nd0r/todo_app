from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from todo import app, db

Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run(host='localhost', port=5005):
    app.run(host=host, port=port)
