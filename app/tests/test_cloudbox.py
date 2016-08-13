import os, tempfile
import pytest, requests
from flask_sqlalchemy import SQLAlchemy
from unittest import TestCase, skip

from app import db, service, settings
from app.cloudbox.factories import DocumentFactory
from app.config import configure_service
from app.factory import create_app
from app.models import Document
from sqlalchemy.orm.session import Session


@pytest.fixture(scope="session")
def test_app():
    # Use: @pytest.mark.usefixtures("test_app")
    _app = create_app('testing')
    db.init_app(_app)
    # configure_service(_app, 'testing')
    ctx = _app.app_context()
    ctx.push()
    _app.logger.info("Test Context: %s", ctx)
    with ctx as c:
        db.create_all()

    def teardown():
        ctx.pop()
        db.drop_all()
    # request.addfinalizer(teardown)
    return _app
    # yield 

    # ctx.pop()
    # db.drop_all()


class TestCloudBox(TestCase):
    """
    Re-run tests. They are returning 404s even when pages
    are loading.
    """
    def setUp(self):
        self.app = service.test_client()
        self.app.testing = True

    def tearDown(self):
        pass
        # db.session.remove()
        # db.drop_all()

    # @pytest.mark.usefixtures("test_app")
    def test_renders_index(self):
        response = requests.get('http://localhost:5000/documents')

        self.assertEqual(response.status_code, 200)

    @skip("Skip upload document")
    def test_upload_document(self):
        f = open('app/tests/support/test_upload.txt')
        doc = f.read()
        f.close()
        response = self.app.post('/documents', data=doc)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
