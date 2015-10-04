import os
import unittest
import tempfile
import mainApp

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        mainApp.app.config['TESTING'] = True
        self.mainApp = mainApp.app.test_client()

    def test_index(self):
        index = self.mainApp.get('/')
        assert 'Hello World' in index.data

if __name__ == '__main__':
    unittest.main()