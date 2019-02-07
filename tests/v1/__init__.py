import unittest

from app import create_app
from config import app_config


class InputTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(app_config)
        self.client = self.app.test_client()

    def tearDown(self):
        self.app.testing = False
