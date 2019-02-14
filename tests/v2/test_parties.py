import unittest
import json
import os
from app import create_app

from base_tests import TestBaseClass

class TestParties(TestBaseClass):
     
    #  def test_error_create_party(self):
    #     response= self.client.post('api/v2/party',data=json.dumps(self.PARTY),
    #     content_type='application/json')
    #     # result=json.loads(response.data.decode())
       
    #     self.assertEqual(response.status_code, 401)

     def test_error_create_party(self):
        response = self.client.get('{}/party'.format(self.endpoint),data=json.dumps(self.PARTY),
        content_type='application/json')
        self.assertEqual(response.status_code, 401)
     def test_empty_list_party(self):
        response = self.client.get('{}/party'.format(self.endpoint),data=json.dumps(self.EMPTY_PARTY),
        content_type='application/json')
        # res=json.loads(response.data.decode('utf-8'))
        
        self.assertEqual(response.status_code, 401)
     def test_delete_party(self):
        response= self.client.get('{}/party'.format(self.endpoint), data=json.dumps(self.PARTY),
        content_type='application/json')
        # result= json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 401)
     def test_get_specific_party(self):
        response= self.client.get('{}/party/1'.format(self.endpoint), data=json.dumps(self.PARTY),
        content_type='application/json')
        # result= json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 405)
        
