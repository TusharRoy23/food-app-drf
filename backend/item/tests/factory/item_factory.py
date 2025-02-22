from factory import SubFactory
from factory.fuzzy import FuzzyChoice

from backend.common.tests.factory.base import BaseFactory
from backend.common.tests.utils.custom_providers import Faker
from backend.item.config import ItemType, ItemFlavor, ItemState, ItemStatus
from backend.item.models import Item
from backend.store.tests.factory.store_factory import StoreFactory


class ItemFactory(BaseFactory):
    store = SubFactory(StoreFactory)
    name = Faker("food")
    item_type = FuzzyChoice(choices=[key for key, _ in ItemType.CHOICES])
    meal_type = FuzzyChoice(choices=[key for key, _ in ItemType.CHOICES])
    meal_state = FuzzyChoice(choices=[key for key, _ in ItemState.CHOICES])
    meal_flavor = FuzzyChoice(choices=[key for key, _ in ItemFlavor.CHOICES])
    price = Faker("price")
    max_order_qty = 0
    min_order_qty = 1
    discount_rate = 0
    status = "active"

    class Meta:
        model = Item
