import requests

from urllib.parse import urljoin


def get_apollo_config(apollo_url=None):
    if not apollo_url:
        from config.settings import APOLLO_URL
        apollo_url = APOLLO_URL
    for i in apollo_url.split(','):
        url = urljoin(i, '/configs/platform/default/common.properties')
        return requests.get(url).json()

