from django.conf import settings
from django.db import models

from .posts import Post
from src.apps.common.model_abstracts import TimedBaseModel


class Comment(TimedBaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_comments",
    )
    
    body = models.TextField()
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self) -> str:
        return f"Comment by {self.author.username} on {self.post}"