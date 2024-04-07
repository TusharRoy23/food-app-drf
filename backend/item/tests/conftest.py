import pytest

from .factory.item_factory import ItemFactory


@pytest.fixture
def item():
    return ItemFactory()


@pytest.fixture
def create_item():
    def _create_item(
        name: str,
        item_type: str,
        meal_type: str,
        meal_state: str,
        meal_flavor: str,
        price: int,
        max_order_qty: int = 0,
        min_order_qty: int = 1,
        discount_rate: int = 0.0,
        status: str = "active",
    ):
        return ItemFactory.create(
            name=name,
            item_type=item_type,
            meal_type=meal_type,
            meal_state=meal_state,
            meal_flavor=meal_flavor,
            price=price,
            max_order_qty=max_order_qty,
            min_order_qty=min_order_qty,
            discount_rate=discount_rate,
            status=status,
        )

    return _create_item


@pytest.fixture
def update_item():
    def _update_item(item: ItemFactory):
        return item.save()

    return _update_item


@pytest.fixture
def item_list():
    return [ItemFactory() for _ in range(10)]
