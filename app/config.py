import logging, os, sys


class Config(object):
    # Why are these not being inherited???
    DEBUG = False

    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'logs/default.log'
    LOGGING_LEVEL = logging.DEBUG

    DATABASE = 'mycloud'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_MYCLOUD']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Production(Config):
    DATABASE = 'mycloud'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_MYCLOUD']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)


class Development(Config):
    DEBUG = True
    DB_NAME = 'mycloud_dev'
    LOGGING_LEVEL = logging.INFO
    # DB_HOST = 'localhost'
    # DB_PORT = '5432'
    # DB_NAME = os.environ['DB_MYCLOUD']
    # DB_USER = os.environ['DB_USER']
    # DB_PWD = os.environ['DB_PASSWORD']
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)


class Testing(Config):
    """Fix DB variables -- not working."""
    DB_NAME = 'mycloud_test'
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = os.environ['DB_MYCLOUD']
    DB_USER = os.environ['DB_USER']
    DB_PWD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME)

config = {
    'default': 'app.config.Development',
    'development': 'app.config.Development',
    'testing': 'app.config.Testing',
    'production': 'app.config.Production'
}

def configure_service(service, env=None):
    """Configures service settings for Flask."""
    global config
    if not env:
        config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    else:
        config_name = env
    service.config.from_object(config[config_name])

    # Logging configuration
    formatter = logging.Formatter(service.config['LOGGING_FORMAT'])
    console_handler = logging.FileHandler(service.config['LOGGING_LOCATION'])
    console_handler.setLevel(service.config['LOGGING_LEVEL'])
    console_handler.setFormatter(formatter)
    service.logger.addHandler(console_handler)
