import factory
from django.utils import timezone

from backend.user.tests.factories import UserFactory

# from factory.faker import Faker
from ..utils.custom_providers import Faker


class LogBaseFactory(factory.django.DjangoModelFactory):
    created_at = timezone.now()
    updated_at = timezone.now()
    created_by = factory.SubFactory(UserFactory)
    updated_by = factory.SubFactory(UserFactory)

    class Meta:
        abstract = True


class BaseFactory(LogBaseFactory):
    code = Faker("unique_code")
    uuid = Faker("uuid")

    class Meta:
        abstract = True
