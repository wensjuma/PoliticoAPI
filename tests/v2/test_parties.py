import unittest
import json
import os
from app import create_app

from base_tests import TestBaseClass

class TestParties(TestBaseClass):
     
   def adminFunction(self):
            return self.client.post(
            "api/v2/parties",
            data=json.dumps(self.PARTY),
            headers={'x-access-token': self.admintoken},
            content_type="application/json")   

   def test_get_specific_party(self):
        response= self.client.get('{}/party/1'.format(self.endpoint), data=json.dumps(self.PARTY),
        content_type='application/json')        
        self.assertEqual(response.status_code, 405)

  