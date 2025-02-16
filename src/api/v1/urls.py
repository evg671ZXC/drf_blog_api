
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from src.api.v1.blog.views import PostViewSet, CommentViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]