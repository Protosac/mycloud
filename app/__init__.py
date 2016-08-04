import logging.config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

service = Flask(__name__)
service.logger.info("LOGGING CONFIGURED")
db = SQLAlchemy(service)

db.create_all()

# View config
from app.views import main

# service.add_url_rule('/', endpoint='main.index', build_only=True)

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
