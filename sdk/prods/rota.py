from datetime import datetime
from django.conf import settings
from django.http.request import HttpRequest
from sdk.utils import send_request


def get_duty_by_date(request: HttpRequest, date: datetime):
    # 将 date 对象转换为 open api 的参数格式（timestamp）
    params = {'date': int(date.timestamp() * 1000)}
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/rota/openapi/v1/date/schedule/list'.format(settings.HOST)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user.apikey:
        params['apikey'] = request.user.apikey
    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('get', url, params=params, cookies=request.COOKIES)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()
