import unittest
import os
import json

# local imports
from app import create_app

from config import app_config
from . import common_func
from app.api.v2.models.database import init_db, drop_table_if_exists
from app.api.v2.models import database


class TestBaseClass(unittest.TestCase):
    """Base test class"""


    def setUp(self):
        self.app = create_app(os.getenv('FLASK_ENV'))
        self.client = self.app.test_client()
        self.app.testing = True
        self.endpoint = "/api/v2"

        self.PARTY = {
        'id':1,
        'party_name': 'Phone Model 1',
        'hqAddress': "hqAddress",
        'logoUrl': 'https//www'
        }
        self.EMPTY_PARTY = {
        'id':1,
        'party_name': '',
        'hqAddress': '',
        'logoUrl': ''
        }

        self.OFFICES = {
                'office_name':'MCA',
                'type':'ward admin'
            }



  
    


if __name__ == '__main__':
    unittest.main()