import unittest
import json
from . import InputTests


class TestParties(InputTests):
    def test_post(self):
         response = self.client.post("api/v1/addparty", data=json.dumps({
                "name": "elihu",
                "slogan": "str"
            }), content_type="application/json")
         result = json.loads(response.data.decode('utf-8'))
         self.assertEqual(result['status'], 201)
    # def test_wrong_post(self):
    #     res = self.client.post("api/v1/addparty", data=json.dumps({
    #             "name": "567890",
    #             "slogan": "3456"
    #         }), content_type="application/json")
    #     result = json.loads(res.data.decode('utf-8'))
    #     self.assertEqual(result['status'], 400)

    def test_get_party(self):
        res=self.client.get("api/v1/getparty")
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['status'], 200)
    def test_empty_list(self):
        res=self.client.get("api/v1/getparty")
        result=json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['data'], [])
