import unittest
from flask import request

from app.api.utils import sanitize_input, validate_string_data_type, return_response
class TestValidators(unittest.TestCase):
#     """define test cases for validations."""
      def test_sanitize_input(self):
          self.assertEqual(sanitize_input("*`92 "), False)

      def test_validate_string_data_type(self):
        self.assertEqual(validate_string_data_type("name"), True)
      def test_return_response(self):
          pass
       

  