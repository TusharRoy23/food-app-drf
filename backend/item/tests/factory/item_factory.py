from factory import SubFactory
from factory.fuzzy import FuzzyChoice

from backend.common.tests.factory.base import BaseFactory
from backend.common.tests.utils.custom_providers import Faker
from backend.item.config import ItemType, MealFlavor, MealState, MealType
from backend.item.models import Item
from backend.restaurant.tests.factory.restaurant_factory import RestaurantFactory


class ItemFactory(BaseFactory):
    restaurant = SubFactory(RestaurantFactory)
    name = Faker("food")
    item_type = FuzzyChoice(choices=[key for key, _ in ItemType.CHOICES])
    meal_type = FuzzyChoice(choices=[key for key, _ in MealType.CHOICES])
    meal_state = FuzzyChoice(choices=[key for key, _ in MealState.CHOICES])
    meal_flavor = FuzzyChoice(choices=[key for key, _ in MealFlavor.CHOICES])
    price = Faker("price")
    max_order_qty = 0
    min_order_qty = 1
    discount_rate = 0
    status = "active"

    class Meta:
        model = Item
