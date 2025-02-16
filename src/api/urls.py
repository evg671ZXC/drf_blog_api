from django.urls import include, path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.routers import DefaultRouter

from src.api.v1.urls import router as v1_router
from api.v1.blog.serializers import PingResponseSerializer


router = DefaultRouter()

@api_view(['GET'])
def ping(request):
    response_data = {"result": True}
    serializer = PingResponseSerializer(data=response_data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


router.registry.extend(v1_router.registry)


urlpatterns = [
    path("ping/", ping),
    path("v1/", include(router.urls)),
]