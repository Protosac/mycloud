
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import factory

from app.config import configure_service
from app.models import db, Document

def create_app(config_name):
    """
    App factory. Can be used to instantiate various environments.
    """
    _app = Flask(__name__)

    configure_service(_app, config_name)
    db.init_app(_app)

    with _app.app_context():
        db.create_all()
	
    return _app


class DocumentFactory(factory.Factory):
    class Meta:
        model = Document

    name = 'testDocument'
    content = 'files/cloudbox/test_doc.txt'
