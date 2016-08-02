import os, tempfile
from unittest import TestCase, skip

from app import db, service, settings
from app.cloudbox.factories import DocumentFactory
from app.models import Document
from sqlalchemy.orm.session import Session


class TestCloudBox(TestCase):
    """
    Re-run tests. They are returning 404s even when pages
    are loading.
    """
    def setUp(self):
        service.config.from_object(settings.Testing)
        db.create_all()
        self.session = Session()
        self.app = service.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_renders_index(self):
        # Throws: Error Exception on /documents GET
        response = self.app.get('/documents')
        doc = DocumentFactory(name='mydoc')
        doc_list = [doc]

        self.assertEqual(doc.name, 'mydoc')
        self.assertEqual(response.status_code, 200)
        # print(response.data)
        # self.assertEqual(doc_list, response)

    @skip("Skip upload document")
    def test_upload_document(self):
        f = open('app/tests/support/test_upload.txt')
        doc = f.read()
        f.close()
        response = self.app.post('/documents', data=doc)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
