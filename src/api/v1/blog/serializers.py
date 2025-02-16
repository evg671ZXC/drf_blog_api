from rest_framework import serializers

from src.apps.blog.models.posts import Post
from src.apps.blog.models.comments import Comment



class PingResponseSerializer(serializers.Serializer):
    result = serializers.BooleanField()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post