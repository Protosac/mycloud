import logging
from app.config import configure_service
from app import LOGGING, service
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    logging.config.dictConfig(LOGGING)
    service.run()
