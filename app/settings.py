import os, sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Why are these not being inherited???
    DEBUG = False
    DATABASE = 'mycloud'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_MYCLOUD']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Development(Config):
    DEBUG = True
    DB_NAME = 'mycloud_dev'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_MYCLOUD']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
    

class Testing(Config):
    """Fix DB variables -- not working."""
    DB_NAME = 'mycloud_test'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_MYCLOUD']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
