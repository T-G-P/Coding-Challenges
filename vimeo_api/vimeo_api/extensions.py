from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_migrate import Migrate
migrate = Migrate()

from flask.ext.cache import Cache
cache = Cache(config={'CACHE_TYPE': 'redis'})
