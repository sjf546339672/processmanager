#!/usr/bin/env python
import os
import sys
import requests
from config import settings
from config.consts import PORT

try:
    import pymysql
    pymysql.version_info = (1, 3, 14, "final", 0)
    pymysql.install_as_MySQLdb()
except ImportError:
    pass


def register_product():
    url = '{}/tenant/serviceapi/api/v1/product/register'.format(settings.HOST)
    payload = {
        "productNum": settings.PRODUCT_ID,
        "productName": settings.PRODUCT_ID,
        "productUrl": "/{}".format(settings.PRODUCT_ID),
        "description": settings.PRODUCT_NAME
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()


def create_database():
    from config.db import check_mysql_ssl_enabled
    import MySQLdb
    from warnings import filterwarnings
    filterwarnings('ignore', category=MySQLdb.Warning)
    database = settings.DATABASES['default']
    ssl_enabled = check_mysql_ssl_enabled(database['HOST'],
                                          database['USER'],
                                          database['PASSWORD'],
                                          database['PORT'])
    ssl = {}
    if ssl_enabled:
        ssl['check_hostname'] = True
    db = MySQLdb.connect(host=database['HOST'],
                         user=database['USER'],
                         password=database['PASSWORD'],
                         port=database['PORT'],
                         ssl=ssl)
    with db.cursor() as cursor:
        cursor.execute('create database if NOT EXISTS {};'.format(database['NAME']))
    db.commit()


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        register_product()
        create_database()
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_port = PORT
        runserver.default_addr = '0.0.0.0'
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django. Are you sure it's installed and "
                          "available on your PYTHONPATH environment variable? Did you "
                          "forget to activate a virtual environment?")
    execute_from_command_line(sys.argv)
