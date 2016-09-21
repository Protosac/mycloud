import os, logging
import app
from app import cloudbox, db, service
from flask import flash, Flask, jsonify, redirect, request, render_template
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
        """
        500: FileNotFoundError, IsADirectoryError, ValueError
        400: ?

        ValueError: View function did not return a response
        PermissionError
        """
        print("Uploading: %s", request.files)
        f = request.files['uploadDoc']
        if cloudbox.is_valid_ext(f.filename):
            # Store full path to the database
            file_path = 'uploads/cloudbox/' + secure_filename(f.filename)
            file_obj = {
                'content': file_path,
                'name': f.filename
            }
            f.save(file_path)
            doc = cloudbox.save_document(file_obj)

            return "Document saved!"

        else:
            flash("That kind of file isn't allowed.")
            return redirect(request.url)
        

service.add_url_rule('/documents', view_func=DocumentAPI.as_view('document_api'))

