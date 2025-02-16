from django.db import models
from django.contrib.auth.models import AbstractUser

from ..managers import UserAccountManager


class UserAccount(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserAccountManager()

    def __str__(self):
        return self.email