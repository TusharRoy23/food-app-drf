from backend.item.config import ItemType, MealFlavor, MealState, MealType
from backend.item.models import Item


def test_item_model(item):
    assert isinstance(item, Item)


def test_item_create_model(create_item):
    item = create_item(
        name="Vaat",
        item_type=ItemType.FOOD,
        meal_type=MealType.DAILYFOOD,
        meal_state=MealState.HOT,
        meal_flavor=MealFlavor.SWEET,
        price=300,
    )
    assert isinstance(item, Item)
