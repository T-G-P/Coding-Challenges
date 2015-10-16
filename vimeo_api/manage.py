from flask.ext.script import Manager
from flask_migrate import MigrateCommand
from vimeo_api import create_app
from vimeo_api.extensions import db

app = create_app()

manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
