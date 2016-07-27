import os, tempfile
from app import service
from app.cloudbox import factories as cloud_factory
from unittest import TestCase


class TestService(TestCase):
    def setUp(self):
        self.db, service.config['DATABASE'] =  tempfile.mkstemp()
        self.app = service.test_client()

    def tearDown(self):
        os.close(self.db)
        os.unlink(service.config['DATABASE'])

    def test_index_200(self):
        response = self.app.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_list_document(self):
        response = self.app.get('/documents')
        doc = cloud_factory.DocumentFactory()
        doc_list = [doc]

        self.assertEqual(doc.name, 'test_doc.txt')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(doc_list, response.content)

if __name__ == '__main__':
    unittest.main()
