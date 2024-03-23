from django.db.models import Sum

from backend.cart.models import CartItem
from backend.common.services import BaseModelService
from backend.item.services import ItemService


class CartItemService(BaseModelService):
    model = CartItem

    def __init__(self, user=None, *args, **kwargs):
        super(CartItemService, self).__init__(user=user, *args, **kwargs)
        self.item_service = ItemService(user=user)

    def get_cart_item(self, **kwargs):
        return self.item_service.get_item(**kwargs)

    def get_cart_items(self, **kwargs):
        return self.model.objects.filter(**kwargs)

    def __update_cart(self, cart):
        # Import here because of circular dependencies
        from .cart_service import CartService

        cart_service = CartService(user=self.user)

        total_amount = CartItem.objects.filter(cart__uuid=cart.uuid).aggregate(
            total_amount=Sum("total_amount")
        )["total_amount"]
        return cart_service.save_cart(
            cart,
            **{
                "cart_amount": total_amount,
                "total_amount": total_amount,
            }
        )

    def create_cart_item(self, payload):
        self.create(
            **{
                "code": "cart-itm",
                "item": payload.get("item"),
                "cart_id": payload.get("cart").id,
                "quantity": payload.get("quantity"),
                "amount": payload.get("amount"),
                "total_amount": payload.get("total_amount"),
            }
        )
        return self.__update_cart(payload.get("cart"))

    def update_cart_item(self, data):
        cart_item = data.pop("cart_item")
        self.update_model_instance(cart_item, **data)
        self.__update_cart(cart_item.cart)

        return CartItem.objects.get(uuid=cart_item.uuid)

    def delete_cart_item(self, cart_item):
        cart_item.delete()
        self.__update_cart(cart_item.cart)
        return

    def save_cart_item(self, cart, cart_item):
        item = cart_item.get("item")
        qty = cart_item.get("quantity", 0)
        amount = item.price
        total_amount = amount * qty
        payload = {
            "quantity": qty,
            "amount": amount,
            "total_amount": total_amount,
            "item": item,
            "cart": cart,
        }
        cart_item_query = CartItem.objects.filter(
            cart__uuid=cart.uuid, item__uuid=item.uuid
        )
        if cart_item_query.exists():
            result = cart_item_query.get()
            payload["cart_item"] = result
            payload["amount"] = result.amount
            payload["total_amount"] = result.amount * qty
            return self.update_cart_item(payload)
        else:
            return self.create_cart_item(payload)
