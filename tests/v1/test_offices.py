import unittest
import json
from . import InputTests
from . import helper_functions

class OfficeTests(InputTests):
    def test_get_office(self):
        res= self.client.get(
            '{}/office'.format(self.BASE_URL),
            content_type='application/json')
        print res
        self.assertEqual(res.status_code, 200)
        
    def test_return_empty(self):
        res= self.client.get(
            '{}/office'.format(self.BASE_URL),
            content_type='application/json')
        self.assertEqual(helper_functions.convert_response_to_json(
            res)['data'], [])

    def test_specific_office(self):
        """test GET /office/1 - if office doesn't exist """
        res=self.client.get(
            '{}/office/1'.format(self.BASE_URL),
            content_type='application/json'
            )   
        self.assertEqual(res.status_code, 404)
      
    def test_edit_office(self):
        '''test PUT /office/1 -if it doesn't exist'''
        response = self.client.put(
           '{}/office/1'.format(self.BASE_URL),
           content_type ='application/json'
            )
        self.assertEqual(response.status_code, 400)
    def test_unexisting_office_endpoint(self):
    
        """ Test when unexisting url is provided """
        response = self.client.get('api/v1/party/1000')
        self.assertEqual(response.status_code, 404)
    def test_addoffice(self):
        response = self.client.post(
           '{}/office'.format(self.BASE_URL),
           content_type ='application/json'
            )
        self.assertEqual(response.status_code, 400)

