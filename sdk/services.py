from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class HealthSerializer(serializers.Serializer):
    status = serializers.IntegerField(default=200)


health_examples = {
    'application/json': {'status': 200}
}
health_response = openapi.Response('response description', HealthSerializer, examples=health_examples)


@swagger_auto_schema(method="GET", responses={200: health_response})
@api_view(['GET'])
def health_check(request):
    if request.method == 'GET':
        result = {"status": 200}
        return JsonResponse(result)
