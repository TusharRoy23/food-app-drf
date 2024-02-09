from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractUser,
)


class User(AbstractUser):
    """
    User is system
    """
    is_visitor = models.BooleanField(default=True)
    is_restaurant_owner = models.BooleanField(default=False)
    is_restaurant_user = models.BooleanField(default=False)




