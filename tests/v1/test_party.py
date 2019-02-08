import unittest
import json
from . import InputTests
from . import helper_functions


class TestParties(InputTests):
    def test_post(self):
         response = self.client.post("api/v1/party", data=json.dumps({
                "name": "elihu",
                "hqAddress": "str",
                "logoUrl":"url"
            }), content_type="application/json")
         result = json.loads(response.data.decode('utf-8'))
         self.assertEqual(result['status'], 201)
    def test_post_code(self):
         response = self.client.post("api/v1/party", data=json.dumps({
                "name": "elihu",
                "hqAddress": "str",
                "logoUrl":"url"
            }), content_type="application/json")
         
         self.assertEqual(response.status_code, 201)
    
    def test_get_party(self):
        res=self.client.get("api/v1/party")
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['status'], 200)

    def test_empty_list(self):
        res=self.client.get("api/v1/party")
        result=json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['data'], [])

    def test_specific_party(self):
        """test GET /party/1 - if party exists"""
        res=self.client.get(
            '{}/party/1'.format(self.BASE_URL),
            content_type='application/json'
            )   
        self.assertEqual(res.status_code, 200)
        # self.assertEqual(helper_functions.convert_response_to_json(
        #     res)['data'], ['name'])
    
    def test_edit_wrong_party(self):
        '''test PUT /party/1 -if it doesn't exist'''
        response = self.client.put(
           '{}/party/nonexist'.format(self.BASE_URL),
           content_type ='application/json'
            )
        self.assertEqual(response.status_code, 404)
    def test_edit_party(self):
        res=self.client.put(
            '{}/party/1'.format(self.BASE_URL),
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 400)

      
    def test_success_edit_party(self):
        '''test PUT /party/1 -for an existing party'''
        response = self.client.put(
           '{}/party/1'.format(self.BASE_URL),
           content_type ='application/json'
            )
        self.assertEqual(response.status_code, 400)
    
    def test_unexisting_party(self):
        
        """ Test when unexisting url is provided """
        response = self.client.put(
           '{}/party/noexist'.format(self.BASE_URL),
           content_type ='application/json'
            )

        self.assertEqual(response.status_code, 404)
    

    def test_delete_party(self):
        
        """ test for a successiful DELETE  """
        response = self.client.delete(
           '{}/party/0'.format(self.BASE_URL),
           content_type ='application/json'
            )

        self.assertEqual(response.status_code, 400)
    
    def test_deleting_non_existent_party(self):
        res = self.client.delete(
            '{}/parties/1000'.format(self.BASE_URL), content_type="application/json")
        self.assertEqual(res.status_code, 404)
       
    
    


