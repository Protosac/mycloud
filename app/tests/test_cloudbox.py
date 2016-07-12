import os, tempfile
from app import service
from unittest import TestCase
from app.cloudbox import factories
from app import models


class TestCloudBox(TestCase):
    """
    Re-run tests. They are returning 404s even when pages
    are loading.
    """
    def setUp(self):
        self.db, service.config['DATABASE'] =  tempfile.mkstemp()
        self.app = service.test_client()

    def tearDown(self):
        os.close(self.db)
        os.unlink(service.config['DATABASE'])

    def test_renders_index(self):
        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

    def test_upload_document(self):
        f = open('app/tests/support/test_upload.txt')
        doc = f.read()
        f.close()
        response = self.app.post('/documents', data=doc)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
