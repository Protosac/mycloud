import logging.config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from app.factory import create_app
from app.models import db

# service = Flask(__name__)
service = create_app('development')
# db = SQLAlchemy()
db.init_app(service)

with service.app_context():
  db.create_all()

service.logger.info("LOGGING CONFIGURED")

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
