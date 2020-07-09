# coding: utf-8

from rest_framework.viewsets import ModelViewSet
from sdk.rest.authentications import CsrfExemptSessionAuthentication, BasicAuthentication


class ApiModelViewSet(ModelViewSet):
    lookup_url_kwarg = 'id'
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_object(self):
        if 'update' in str(self.request.path_info):
            self.kwargs['id'] = self.request.data['id']
            return super().get_object()
        else:
            self.kwargs['id'] = self.request.query_params['id']
            return super().get_object()





