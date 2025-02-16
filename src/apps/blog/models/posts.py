from taggit.managers import TaggableManager

from django.db import models
from django.conf import settings
from django.utils import timezone

from src.apps.common.model_abstracts import TimedBaseModel


class PublishedManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )

class Post(TimedBaseModel):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date="publish"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)

    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self) -> str:
        return self.title