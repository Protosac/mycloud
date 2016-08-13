import logging
import app
from app import cloudbox, db, service
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


@service.route("/")
def index():
    service.logger.info("LOG - Index rendered.")
    return render_template('index.html')

@service.route("/documents", methods=["GET", "POST", "PUT"])
def documents(doc=None):
    if request.method == "GET":
        res = cloudbox.get_documents()
        return render_template('list.html', documents=res)
    elif request.method == 'POST' and doc:
        # return app.save_document(doc)
        f = request.files['uploaddoc']
        f.save('cloudbox/uploads/' + secure_filename(f.filename))
        return "Successful POST!"
