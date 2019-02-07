import unittest
import json
from . import InputTests

class OfficeTests(InputTests):
    def test_get_office(self):
        res= self.client.get('api/v1/getoffice')
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['status'], 200)

    def test_return_empty(self):
        res= self.client.get('api/v1/getoffice')
        result = json.loads(res.data.decode('utf-8'))
        self.assertEqual(result['data'], [])