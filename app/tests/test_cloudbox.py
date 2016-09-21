import os, tempfile
import pytest, requests
from flask_sqlalchemy import SQLAlchemy
from unittest import TestCase, skip

from app import service, settings
from app.factories import create_app, DocumentFactory
from app.config import configure_service
from app.models import db, Document
from sqlalchemy.orm.session import Session


@pytest.fixture(scope="session")
def test_app():
    # Use: @pytest.mark.usefixtures("test_app")
    _app = create_app('testing')
    
    ctx = _app.app_context()
    ctx.push()
    _app.logger.info("Test Context: %s", ctx)

    def teardown():
        ctx.pop()

    return _app


class TestCloudBox(TestCase):
    """
    Re-run tests. They are returning 404s even when pages
    are loading.

    self.app.app_context() can be used to create models/factories
    when testing controllers.
    """
    def setUp(self):
        self.app = service.test_client()
        self.app.testing = True

    def tearDown(self):
        """The app tears it self down. See init.py"""
        pass

    @pytest.mark.usefixtures("test_app")
    def test_renders_index(self):
        response = requests.get('http://localhost:5000/documents')

        self.assertEqual(response.status_code, 200)

    # @skip("Skip upload document")
    @pytest.mark.usefixtures("test_app")
    def test_upload_document(self):
        localhost = 'http://localhost:5000/documents'
        f = open('app/tests/support/test_upload.txt')
        doc = f.read()
        f.close()
        form = {'name': 'Test Form', 'content': doc}
        response = requests.post(localhost, data=form)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
