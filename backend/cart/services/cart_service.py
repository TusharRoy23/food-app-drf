from backend.cart.models import Cart
from backend.common.services import BaseModelService

from .cart_item_service import CartItemService


class CartService(BaseModelService):
    model = Cart

    def __init__(self, user=None, *args, **kwargs):
        super(CartService, self).__init__(user=user, *args, **kwargs)
        self.cart_item_service = CartItemService(user=user)

    def get_cart(self, **kwargs):
        return self.model.objects.get(**kwargs)

    def get_cart_items(self, **kwargs):
        return self.cart_item_service.get_cart_items(**kwargs)

    def get_store_info(self, **kwargs):
        from backend.store.services import StoreService

        return StoreService().get_store_info(**kwargs)

    def create_cart(self, cart):
        cart_item = cart.pop("item")
        item = cart_item.get("item")
        cart = self.create(
            **cart, store=item.store, user=self.user, code="cart"
        )
        return self.cart_item_service.save_cart_item(cart=cart, cart_item=cart_item)

    def update_cart(self, cart, cart_item):
        cart_item = cart_item.pop("item")
        return self.cart_item_service.save_cart_item(cart=cart, cart_item=cart_item)

    def save_cart(self, cart, **data):
        self.update_model_instance(cart, **data)
        return self.get_cart(uuid=cart.uuid)
