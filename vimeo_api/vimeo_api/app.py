from flask import Flask, jsonify
from .config import DefaultConfig
from .api import api
from .extensions import db, migrate
import os

DEFAULT_BLUEPRINTS = {api}


def create_app(config=None, app_name=None, blueprints=None):

    if app_name is None:
        app_name = DefaultConfig.PROJECT

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__)
    configure_app(app, os.environ['APP_SETTINGS'])
    configure_extensions(app)
    configure_blueprints(app, blueprints)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(os.environ['APP_SETTINGS'])

    if config:
        app.config.from_object(config)


def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)

    # flask-migrate
    migrate.init_app(app, db)


def configure_blueprints(app, blueprints):
    # only one blueprint in this case, but
    # extensible for many
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(error='Bad Request'), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify(error='Unauthorized'), 401

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error='Not Found'), 404

    @app.errorhandler(410)
    def gone(error):
        return jsonify(error='Gone'), 410
