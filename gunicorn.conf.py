import multiprocessing
from config.consts import PRODUCT_ID, PORT
worker_class = 'eventlet'
bind = f"0.0.0.0:{PORT}"   #绑定的ip与端口
workers = 2                #核心数
#loglevel = 'debug'   #日志等级
proc_name = f'devcenter_{PRODUCT_ID}_gunicorn'   #进程名
