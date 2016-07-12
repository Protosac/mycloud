from flask_sqlalchemy import SQLAlchemy 
from flask import Flask 

service = Flask(__name__)
service.config.from_object('settings.Development')
db = SQLAlchemy(service)

db.create_all()
