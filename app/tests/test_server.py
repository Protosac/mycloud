import os, tempfile
from app import service
from app.cloudbox import factories as cloud_factory
from unittest import TestCase, skip


class TestService(TestCase):
    def setUp(self):
        self.db, service.config['DATABASE'] =  tempfile.mkstemp()
        service.config['TESTING'] = True
        self.app = service.test_client()

    def tearDown(self):
        os.close(self.db)
        os.unlink(service.config['DATABASE'])

    def test_index_200(self):
        response = self.app.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
