from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

from app.config import configure_service

def create_app(config_name):
	_app = Flask(__name__)
	configure_service(_app, config_name)
	
	return _app
