
"""
    Contains the base test class for the
    other test classes
"""
import unittest

from app import create_app
from config import app_config
from . import helper_functions
import json

class InputTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(app_config)
        self.client = self.app.test_client()
        self.app.testing = True
        self.BASE_URL= 'api/v1'
        self.PARTY={
            'name':'urp',
            'hqAddress':'nairobi',
            'logoUrl':'www.url'
        }
        
        self.OFFICE={
            'name':'justine',
            'type':'admin'
        }
    

    def tearDown(self):
        self.app.testing = False

class TestInvalidRoutes(InputTests):
    def test_invalid_route(self):
        response = self.client.get("api/rNotFound")
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["error"], "url not found")
        self.assertEqual(result["status"], 404)
