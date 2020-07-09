# coding: utf-8

from django.test import TestCase
from rest_framework.test import APIClient


class TestApi(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_hello(self):
        self.result = {'message': 'Hello World'}
        with self.settings(LOCAL_DEV=True):
            response = self.client.get('/frontapi/v1/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.result)
