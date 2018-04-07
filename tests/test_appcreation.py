import os
import unittest
import tempfile
import warnings

from app import create_app

class AppCreationTestCase(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore")

    def tearDown(self):
        pass

    def test_create_app_with_no_options_raises_exception(self):
        with self.assertRaises(ValueError):
            app = create_app(None)    

    def test_create_app_with_invalid_config_path(self):
        with self.assertRaises(FileNotFoundError):
            app = create_app('../config/appsettings.json')

    def test_create_app_with_int_config_path(self):
        with self.assertRaises(ValueError):
            app = create_app(102)
