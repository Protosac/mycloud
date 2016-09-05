import logging.config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from app.factory import create_app
from app.models import db

service = create_app('development')
service.logger.info("Starting service ...")

@service.teardown_appcontext
def shutdown_session(exception=None):
  db.session.remove()

# View config
from app.views import index

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
              'filename': 'logs/mycloud.log',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['logs', 'console'],
        'level': logging.INFO,
        },
)
