import logging
import app
from app import cloudbox, db, service
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

if __name__ == '__main__':
    logging.config.dictConfig(app.LOGGING)
    service.run()
