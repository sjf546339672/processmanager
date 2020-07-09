# coding: utf-8
import time

import requests
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from sdk.prods import Automation

from .serializers import HelloSerializer
from sdk.prods import ant

hello_examples = {
    'application/json': {'message': "Hello World"}
}
hello_response = openapi.Response('response description', HelloSerializer, examples=hello_examples)


@swagger_auto_schema(method="GET", responses={200: hello_response})
@api_view(['GET'])
def hello(request):
    result = {"message": "Hello World"}
    return JsonResponse(result)


@api_view(['GET'])
def query_os(request):
    query_list = ant.query_os(request)
    os_info = [
        {
            'key': index + 1,
            'name': host['name'],
            'id': host['id'],
            'ip': host['ip'],
            'os': host['type'],
            'status': '在线' if host['agent']['state'] == "online" else '离线'
        }
        for index, host in enumerate(query_list)
    ]
    return JsonResponse({"message": os_info})


@api_view(['GET'])
def get_processes(request, agent_id):
    # 调用automaiton执行操作api，执行show_processes操作（获取系统进程）
    # result = ant.execute_action(request, 'show_processes', request.GET.get('agentId'), {})
    print("===================agent_id", agent_id)
    result = ant.execute_action(request, 'show_processes', agent_id, {})
    # 调用automation查询作业详情api，获取task信息
    job_info = ant.get_job(request, result['id'])
    task = job_info['tasks'][0]
    # 调用automation获取执行参数api，获取task输出参数（即执行结果）
    task_output_param, done, task_status = ant.quick_get_task_output_param(request, task['id'])
    # 每隔两秒获取一次执行结果，直到task执行完成
    print(111111111111, task_output_param, done, task_status)
    while not done:
        time.sleep(2)
        task_output_param, done, task_status = ant.quick_get_task_output_param(request, task['id'])
    return JsonResponse({"message": json.loads(task_output_param['result'])})


@api_view(['GET'])
def kill_process(request, agent_id, pid):
    # 调用automaiton执行操作api，执行kill_process操作（杀死进程）
    result = ant.execute_action(request, 'kill_process', str(agent_id), {'pid': int(pid)})
    # 调用automation查询作业详情api，获取task信息
    job_info = ant.get_job(request, result['id'])
    task = job_info['tasks'][0]
    # 调用automation获取执行参数api，获取task输出参数（即执行结果）
    task_output_param, done, task_status = ant.quick_get_task_output_param(request, task['id'])
    # 每隔两秒获取一次执行结果，直到task执行完成
    while not done:
        time.sleep(2)
        task_output_param, done, task_status = ant.quick_get_task_output_param(request, task['id'])
    return JsonResponse({"message": json.loads(task_output_param['result'])})











































