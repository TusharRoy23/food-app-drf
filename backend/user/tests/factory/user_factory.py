from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from backend.common.tests.utils.custom_providers import Faker

User = get_user_model()


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password")
    first_name = Faker("name")
    last_name = Faker("name")
    is_active = True
    is_staff = False
    is_superuser = False
    is_visitor = True

    class Meta:
        model = User
        django_get_or_create = ["username", "email"]
