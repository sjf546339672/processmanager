from django.http import HttpResponse
from django.conf import settings
from urllib.parse import urljoin
import json

import requests

requests_session_map = {}


def send_request(method,
                 url,
                 headers=None,
                 data=None,
                 cookies=None,
                 params=None) -> requests.Response:
    response = getattr(requests, method)(url, headers=headers, json=data, cookies=cookies, params=params)
    return response


class Session:

    def __init__(self, request):
        self._request = request

    def get(self, path, headers=None, params=None):
        path, params = self._handle_path_and_params(path, params)
        response = requests.get(path, headers=headers, cookies=self._request.COOKIES, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, path, headers=None, data=None, params=None):
        path, params = self._handle_path_and_params(path, params)
        response = requests.post(path,
                                 headers=headers,
                                 cookies=self._request.COOKIES,
                                 json=data,
                                 params=params)
        response.raise_for_status()
        return response.json()

    def _handle_path_and_params(self, path, params):
        path = urljoin(settings.HOST, path)
        if 'token' not in self._request.COOKIES and hasattr(self._request.user, 'apikey'):
            params['apikey'] = self._request.user.apikey
        return path, params
