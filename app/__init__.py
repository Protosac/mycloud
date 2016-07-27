import logging.config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

service = Flask(__name__)
service.config.from_object('settings.Development')
service.logger.info("LOGGING CONFIGURED")
db = SQLAlchemy(service)

db.create_all()

LOGGING = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'console': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.INFO},
        'logs': {'class': 'logging.handlers.RotatingFileHandler',
              'formatter': 'f',
              'filename': 'log',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['logs', 'console'],
        'level': logging.INFO,
        },
)
