import logging
import app
from app import cloudbox, db, service
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

# from app.cloudbox import app

@service.route("/")
def index():
    service.logger.info("LOG - Index rendered.")
    return render_template('index.html')

@service.route("/documents", methods=["GET", "POST", "PUT"])
def documents(doc=None):
    if request.method == "GET":
        return "Successful GET!"
        # return cloudbox.get_documents()
    elif request.method == 'POST' and doc:
        # return app.save_document(doc)
        return "Successful POST!"


if __name__ == '__main__':
    logging.config.dictConfig(app.LOGGING)
    service.run()
