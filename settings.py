import os, sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    DATABASE = 'mycloud'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    DB_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Development(Config):
    DEBUG = True
    DB_NAME = 'mycloud_dev'
    

class Testing(Config):
    DB_NAME = 'mycloud_test'