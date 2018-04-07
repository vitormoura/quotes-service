from flask import json

import os
import unittest
import tempfile
import warnings

from app import create_app


class QuotesServiceTestCase(unittest.TestCase):

    def setUp(self):

        warnings.simplefilter("ignore")

        self.temp_fd, self.temp_dbfile = tempfile.mkstemp()

        test_options = dict(
                {'SQLALCHEMY_DATABASE_URI':
                    'sqlite:///{}'.format(self.temp_dbfile)}
        )

        myapp=create_app(test_options)
        myapp.testing=True

        self.app=myapp.test_client()

    def tearDown(self):

        os.close(self.temp_fd)
        os.unlink(self.temp_dbfile)

    def test_create_category(self):

        resp=self.app.post('/quotes/categories', data = dict(id=1,
                                                             description='a sample category', acronym='samples'))

        self.assertEqual(resp.status_code, 200)

        data=json.loads(resp.data)

        self.assertTrue(data is not None)
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['acronym'], 'samples')

    def test_empty_categories(self):
        rv=self.app.get('/quotes/categories')
        data=json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(0, len(data))       
