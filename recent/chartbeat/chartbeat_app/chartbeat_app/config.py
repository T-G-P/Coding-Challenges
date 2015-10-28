import os


class DefaultConfig(object):
    PROJECT = 'chartbeat_api'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(DefaultConfig):
    DEBUG = False


class StagingConfig(DefaultConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(DefaultConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(DefaultConfig):
    TESTING = True

print(os.environ['DATABASE_URL'])
