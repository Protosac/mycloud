import os, tempfile
from app import service
from app.cloudbox import factories as cloud_factory
from unittest import TestCase


class TestModels(TestCase):
    """Test custo model methods."""
    def setUp(self):
        self.db, service.config['DATABASE'] =  tempfile.mkstemp()

    def tearDown(self):
        os.close(self.db)
        os.unlink(service.config['DATABASE'])

    def test_index_200(self):
        

if __name__ == '__main__':
    unittest.main()
