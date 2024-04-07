from backend.common.tests.factory.base import BaseFactory
from backend.common.tests.utils.custom_providers import Faker
from backend.restaurant.models import Restaurant


class RestaurantFactory(BaseFactory):
    name = Faker("company_suffix")
    address = Faker("city")
    picture = "https://www.google.com"
    opening_time = "08:00:00"
    closing_time = "00:00:00"
    status = "active"

    class Meta:
        model = Restaurant
