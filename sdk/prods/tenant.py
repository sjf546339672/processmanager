import logging
import requests

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.http import HttpRequest
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from ..utils import send_request

logger = logging.getLogger('sdk')
sessions = {}


class User(AbstractUser):

    class Meta:
        abstract = True

    def __str__(self):
        return f'<User {self.username}>'


class AuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if '/admin/' not in request.path and 'serviceapi' not in request.path and 'swagger' not in request.path and 'redoc' not in request.path and 'health_check' not in request.path and not request.path.startswith('/favicon.ico'):
            if not request.session.session_key:
                request.session.cycle_key()
            if request.session.session_key in sessions:
                request.user = sessions[request.session.session_key]
            if not (hasattr(request, 'user') and isinstance(request.user, User)):
                request.user = Tenant.get_user_info(request)
                if not request.user:
                    return redirect(
                        f'{settings.HOST}/tenant/#/login_admin?return_insite={settings.HOST}/{settings.PRODUCT_ID}{request.path}'
                    )
                else:
                    sessions[request.session.session_key] = request.user


class Tenant(object):

    @classmethod
    def get_user_info(cls, request: HttpRequest):
        if settings.LOCAL_DEV:
            return User(username='admin', is_active=True, is_staff=True, email='admin@example.com',
                        first_name='admin')
        headers = {}
        url = '{}/tenant/api/v1/user/details/view'.format(settings.HOST)

        cookies = request.COOKIES
        cookies['language'] = 'zh_CN'
        try:
            response = send_request('get', url, headers=headers, cookies=cookies)
            response.raise_for_status()
            data = response.json().get('data')
            user = User(username=data.get('userNo'), is_active=True, is_staff=True, email=data.get('email'),
                        first_name=data.get('realname'))
        except requests.exceptions.HTTPError as e:
            if e.response.status_code != 401:
                logger.error(f'[Tenant] get user info failed: {e}', exc_info=1)
            return None
        except Exception as e:
            logger.error(f'[Tenant] get user info failed: {e}', exc_info=1)
            return None
        else:
            return user
