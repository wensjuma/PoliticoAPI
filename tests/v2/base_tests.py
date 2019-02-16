import unittest
import os
import json


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
        'id':2,
        'party_name': 'Phone Modelew 1',
        'hqAddress': "hqAddressew",
        'logoUrl': 'https//wwww'
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

        self.admintoken= {"qwasdgrwertgpADFwplse4WEadgFGTle5yuui7nklofdhklowqvmlpufwwn"}
        self.NEWUSER={
                "firstname":"just",
                "lastname":"scrud",
                "username":"wesres2",
                "othername":"mike",
                "email":"mike@gmail.com",
                "phone":"0789675438",
                "passportUrl":"https",
                "password":"password",
                "retypedpassword":"password",
                "isPolitician":False 
          }
        self.EMPTY_USER={
                "firstname":"",
                "lastname":"",
                "username":"",
                "othername":"",
                "email":"",
                "phone":"",
                "passportUrl":"",
                "password":"",
                "retypedpassword":"",
                "isPolitician":False 
          }

        self.TEST_LOGIN={
                'email':'',
                'password':''
          }
        self.VOTING={
                 'created_by':'jusmine',
                 'office':'mps',
                 'candidate':'joshua'
          }
    def tearDown(self):
            self.app.testing = False

class TestInvalidRoutes(TestBaseClass):
    def test_invalid_route(self):
        response = self.client.get("api/rNotFound")
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result["error"], "url not found")
        self.assertEqual(result["status"], 404)



if __name__ == '__main__':
    unittest.main()