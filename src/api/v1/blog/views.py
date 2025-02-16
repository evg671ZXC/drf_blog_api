# Create your views here.
from rest_framework import viewsets

from src.apps.blog.models import Post
from src.apps.blog.models import Comment
from .serializers import PostSerializer
from .serializers import CommentSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
