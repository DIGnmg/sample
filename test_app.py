import os
import unittest
import tempfile
import app

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_index(self):
        index = self.app.get('/')
        assert 'Hello world' in index.data

if __name__ == '__main__':
    unittest.main()