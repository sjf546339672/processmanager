import os

from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render

from sdk.services import health_check


def index(request):
    frontend_index = os.path.join(settings.FRONTEND_DIR, 'index.html')
    return render(request, frontend_index)


urlpatterns = [
    url(r'health_check', health_check),
    url(r'^$', index),
]
