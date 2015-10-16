import os


class DefaultConfig(object):
    PROJECT = 'vimeo_api'
    DEBUG = False
    TESTING = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    CSRF_ENABLED = True
    UPLOAD_FOLDER = '/tmp/files'
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
