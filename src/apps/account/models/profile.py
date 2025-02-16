from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin

from src.apps.common.model_abstracts import TimedBaseModel
from src.apps.account.entities import Profile as ProfileEntity


class Profile(TimedBaseModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)

    location = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    photo = models.ImageField(
        upload_to='users/%Y/%m/%d/',
        blank=True,
    )
    
    def __str__(self):
        return f'Profile of {self.user.username}'
    
    def to_entity(self) -> ProfileEntity:
        return ProfileEntity(
            id=self.pk,
            username=self.user.username,
            email=self.user.email,
            bio=self.bio,
            location=self.location,
            date_of_birth=self.date_of_birth,
            photo=self.photo,
            updated_at=self.updated_at,
            created_at=self.created_at,
        )


    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'