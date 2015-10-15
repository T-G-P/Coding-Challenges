import os


class DefaultConfig(object):
    PROJECT = 'vimeo_api'
    DEBUG = False
    TESTING = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    CSRF_ENABLED = True
    UPLOAD_FOLDER = '/tmp/files'


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

