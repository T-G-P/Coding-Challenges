from flask.ext.script import Manager
from flask_migrate import MigrateCommand
from chartbeat_app import create_app
from chartbeat_app.extensions import db
from chartbeat_app.api import Host
from chartbeat_app.utils import chartbeat_request
import requests_cache
import datetime

app = create_app()

manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def populate_top_pages():
    """
    This goes through the domains stored locally and gets the
    latest chartbeat data everh hour
    """
    requests_cache.clear()
    for host_obj in Host.query.all():
        api_key = host_obj.api_key.api_key
        host_name = host_obj.host_name
        res = chartbeat_request(api_key, host_name)
        host_obj.top_pages = res.json()
        host_obj.updated_at = datetime.datetime.utcnow()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
