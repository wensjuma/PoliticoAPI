import unittest
import json
from . import InputTests
from . import helper_functions
from app.api.v1.models.data_model import OFFICES

class OfficeTests(InputTests):
    def test_add_office(self):
        res = self.client.post(
            "api/v1/offices", data=json.dumps(self.OFFICE), 
            content_type="application/json")
        # result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(len(OFFICES), 0)
    def test_get_office(self):
        res= self.client.get(
            '{}/office'.format(self.BASE_URL),
            content_type='application/json')
       
        self.assertEqual(res.status_code, 200)
        
    def test_return_empty(self):
        res= self.client.get(
            '{}/office'.format(self.BASE_URL),
            content_type='application/json')
        self.assertEqual(helper_functions.convert_response_to_json(
            res)['data'], [])

    def test_specific_office(self):
        """test GET /office/0 - if office doesn't exist """
        res=self.client.get(
            '{}/office/1'.format(self.BASE_URL),
            content_type='application/json'
            )   
        self.assertEqual(res.status_code, 200)
             
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
    def test_save_valid_office_type(self):
            res = self.client.post("api/v1/office", data=json.dumps({
            "type": "type",
            "name": "name"
            }), content_type="application/json"
            )
            self.assertEqual(res.status_code, 201)
   
          

