import unittest
from unittest.mock import patch

from sqlalchemy import null

import app

class CURDTEST(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.payload = {'its': 'empty'}
    
    def test_home(self):
        response = self.client.post("/", data={
        "word": "Flask"
        })
        assert response.status_code == 200
    
    def test_update(self):
        response = self.client.post("/update", data={
        "word1": "Flask",
        "word2": "APP"
        })
        assert response.status_code == 200

    def test_delete(self):
        response = self.client.post("/delete", data={
        "word": "Flask"
        })
        assert response.status_code == 200