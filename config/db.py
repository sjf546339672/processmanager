import pymysql


def check_mysql_ssl_enabled(host, user, password, port):
    try:
        client = pymysql.connect(host=host, user=user, password=password,
                                 port=int(port))
        client.close()
    except pymysql.err.OperationalError:
        return True
    else:
        return False
