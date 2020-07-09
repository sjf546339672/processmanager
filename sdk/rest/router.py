# coding: utf-8
from rest_framework.routers import Route, DynamicRoute, DefaultRouter


class ApiRouter(DefaultRouter):
    routes = [
        # List route.
        Route(
            url=r'^{prefix}/query{trailing_slash}$',
            mapping={
                'get': 'list',
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),

        Route(
            url=r'^{prefix}/create$',
            mapping={
                'post': 'create',
            },
            name='{basename}-create',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),

        Route(
            url=r'^{prefix}/delete$',
            mapping={
                'post': 'destroy',
            },
            name='{basename}-delete',
            detail=True,
            initkwargs={'suffix': 'Delete'}
        ),

        Route(
            url=r'^{prefix}/update$',
            mapping={
                'post': 'partial_update',
            },
            name='{basename}-update',
            detail=True,
            initkwargs={'suffix': 'Update'}
        ),

        Route(
            url=r'^{prefix}/search',
            mapping={
                'get': 'search',
            },
            name='{basename}-search',
            detail=True,
            initkwargs={'suffix': 'Search'}
        ),

        DynamicRoute(
            url=r'^{prefix}/{url_path}{trailing_slash}$',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),

        # 'get': 'retrieve',
        # 'put': 'update',
        # 'patch': 'partial_update',
        # 'delete': 'destroy'
    ]

