import os
import unittest
import tempfile
import mainApp

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        mainApp.mainApp.config['TESTING'] = True
        self.mainApp = mainApp.mainApp.test_client()

    def test_index(self):
        index = self.mainApp.get('/')
        assert 'mainApp' in index.data

if __name__ == '__main__':
    unittest.main()