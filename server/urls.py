from django.urls import path

from . import services


urlpatterns = [
    path("frontapi/v1/hello/", services.hello),
    path("frontapi/v1/queryOS/", services.query_os),
    path("frontapi/v1/<str:agent_id>/", services.get_processes),
    path("frontapi/v1/<str:agent_id>/<int:pid>/", services.kill_process),
]
