import logging
import app
from app import cloudbox, db, service
from flask import Flask, jsonify, request, render_template
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


@service.route("/")
def index():
    service.logger.info("LOG - Index rendered.")
    return render_template('index.html')


class DocumentAPI(MethodView):

    def get(self):
        docs = cloudbox.get_documents()
        return render_template('list.html', documents=docs)

    def post(self):
        print("REQUEST.FILES: %s", request.form)
        f = request.files['uploadDoc']
        file_path = 'uploads/'+ secure_filename(f.filename)
        file_obj = {
            'content': file_path,
            'name': request.form['docName']
        }

        try:
            f.save(file_path)
            doc = cloudbox.save_document(file_obj)
        except:
            # PermissionError
            raise
        else:
            return "Document saved!"

service.add_url_rule('/documents', view_func=DocumentAPI.as_view('document_api'))

