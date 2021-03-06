"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import site

from config import consts
from django.core.wsgi import get_wsgi_application

site.addsitedir(consts.PACKAGE_SITE_DIR)

try:
    import pymysql
    pymysql.version_info = (1, 3, 14, "final", 0)
    pymysql.install_as_MySQLdb()
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
