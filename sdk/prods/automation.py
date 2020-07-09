from django.conf import settings
from django.http.request import HttpRequest
from sdk.utils import send_request

AutomationTaskStatusMap = {
    0: "等待执行",
    1: "执行中",
    2: "执行成功",
    7: "已取消",
    8: "执行中断",
    9: "执行错误",
    10: "系统中断",
    11: "跳过"
}
AutomationTaskRunningStatus = [0, 1]


def query_hosts(request: HttpRequest, key=None, zone_id=None):
    # 默认情况下会返回所有的主机
    params = {}
    if key:
        # 名称，ip，标签
        params['key'] = key
    if zone_id:
        # zone_id 是上级 hub 的 agent id, 可以从 config.yaml 里看到
        params['zone_id'] = zone_id
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/automation/boltdog/openapi/v2/resources/hosts/query'.format(settings.HOST)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user and hasattr(
            request.user, 'apikey'):
        params['apikey'] = request.user.apikey

    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('get', url, cookies=request.COOKIES, params=params)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()


def execute_action(request: HttpRequest, action_code: str, agent_id: str, args: dict):
    params = {
        'id': action_code,
    }
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/automation/boltdog/openapi/v2/jobs/execute-action'.format(settings.HOST)
    payload = {'_host': [{"type": "id", "value": agent_id}]}
    payload.update(args)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user and hasattr(
            request.user, 'apikey'):
        params['apikey'] = request.user.apikey

    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('post', url, cookies=request.COOKIES, params=params)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()


def get_job(request: HttpRequest, job_id: str):
    params = {
        'id': job_id,
    }
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/automation/boltdog/openapi/v2/jobs/get'.format(settings.HOST)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user and hasattr(
            request.user, 'apikey'):
        params['apikey'] = request.user.apikey

    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('get', url, cookies=request.COOKIES, params=params)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()


def get_task(request: HttpRequest, task_id: str):
    params = {
        'id': task_id,
    }
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/automation/boltdog/openapi/v2/jobs/tasks/get'.format(settings.HOST)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user and hasattr(
            request.user, 'apikey'):
        params['apikey'] = request.user.apikey

    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('get', url, cookies=request.COOKIES, params=params)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()


def get_task_log(request: HttpRequest, execute_task_id: str):
    params = {
        'id': execute_task_id,
    }
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/automation/boltdog/openapi/v2/jobs/tasks/logs/query'.format(settings.HOST)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user and hasattr(
            request.user, 'apikey'):
        params['apikey'] = request.user.apikey

    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('get', url, cookies=request.COOKIES, params=params)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()


def get_task_params(request: HttpRequest, execute_task_id: str):
    params = {
        'id': execute_task_id,
    }
    # 从 settings.py 获取，优云 PASS 平台地址
    url = '{}/automation/boltdog/openapi/v2/jobs/tasks/params/query'.format(settings.HOST)

    # 优云 PASS Open api 主要通过 apikey 来做认证，用户登录时，可以直接从 cookies 中提取 token 转换为 apikey
    if 'token' not in request.COOKIES and request and request.user and hasattr(
            request.user, 'apikey'):
        params['apikey'] = request.user.apikey

    # 使用 requests 向优云 PASS Open api 发起请求
    response = send_request('get', url, cookies=request.COOKIES, params=params)
    # 如果请求 PASS open api 出现错误请求，就抛出异常，由外部处理
    response.raise_for_status()
    #  请求成功后，返回请求数据
    return response.json()


def quick_get_task_log(request: HttpRequest, task_id: str):
    # 快速获取任务执行日志
    # 内部通过调用 automation 的两个接口实现，
    # 1. get_task 获取任务执行 id
    # 2. get_task_log 获取任务执行日志
    task_info = get_task(request, task_id)
    task_log = ''
    status = ''
    done = False

    if len(task_info['host_exec_infos']):
        execute_host_info = task_info['host_exec_infos'][0]
        if execute_host_info['status'] not in AutomationTaskRunningStatus:
            task_log = get_task_log(request, execute_host_info['id'])['msg']
            status = AutomationTaskStatusMap.get(execute_host_info['status'], '未知状态')
            done = True
        else:
            status = AutomationTaskStatusMap.get(execute_host_info['status'], '未知状态')
    return task_log, done, status


def quick_get_task_output_param(request: HttpRequest, task_id: str):
    # 快速获取任务执行输出参数
    # 内部通过调用 automation 的两个接口实现，
    # 1. get_task 获取任务执行 id
    # 2. get_task_params 获取任务执行参数
    task_info = get_task(request, task_id)
    task_output_param = ''
    status = ''
    done = False

    if len(task_info['host_exec_infos']):
        execute_host_info = task_info['host_exec_infos'][0]
        if execute_host_info['status'] not in AutomationTaskRunningStatus:
            task_output_param = get_task_params(request, execute_host_info['id'])['output_param']
            status = AutomationTaskStatusMap.get(execute_host_info['status'], '未知状态')
            done = True
        else:
            status = AutomationTaskStatusMap.get(execute_host_info['status'], '未知状态')
    return task_output_param, done, status
