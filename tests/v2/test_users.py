import unittest
import json
import os
from app import create_app
from base_tests import TestBaseClass




class TestUsers(TestBaseClass):

 def test_user_create_account_empty(self):
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.EMPTY_USER), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result["status"], 400)
        


 def test_user_creating_account_duplicate(self):
        response = self.client.post('api/v2/auth/signup', data=json.dumps(self.NEWUSER), 
        content_type='application/json')
        self.assertEqual(response.status_code, 409)
        
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result["status"], 409)
 def test_failing_login(self):
        response = self.client.post('api/v2/auth/signin', data=json.dumps(self.TEST_LOGIN), 
        content_type='application/json')
        self.assertEqual(response.status_code, 400)
        
        result = json.loads(response.data.decode("utf-8"))
        self.assertEqual(result["status"], 400)