from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """
    User is system
    """

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=True)

    objects = CustomUserManager()
