from backend.cart.config import CartStatus
from backend.cart.services import CartService
from backend.common.services import BaseModelService
from backend.order.models import Order
from backend.store.services.store_notification_service import (
    StoreNotificationService,
)

from .order_item import OrderItemService


class OrderService(BaseModelService):
    model = Order

    def __init__(self, user=None, *args, **kwargs):
        super(OrderService, self).__init__(user=user, *args, **kwargs)
        self.cart_service = CartService(user=user)
        self.order_item_service = OrderItemService(user=user, *args, **kwargs)

    def get_order(self, **kwargs):
        return self.model.objects.get(**kwargs)

    def __send_notification_to_store(self, order: Order):
        StoreNotificationService(code=order.store.code).send_notification(
            **{"message": f"New Order {order.code}"}
        )

    def create_order(self, data):
        cart = self.cart_service.get_cart(
            uuid=data.get("uuid"), user__id=self.user.id, status=CartStatus.SAVED
        )
        cart_items = cart.cartitem_cart.all()
        order = self.create(
            user=cart.user,
            store=cart.store,
            order_amount=cart.cart_amount,
            code="odr",
        )

        result = self.order_item_service.create_order_item(
            order=order, cart_items=cart_items
        )
        self.cart_service.save_cart(cart, **{"status": CartStatus.APPROVED})
        self.__send_notification_to_store(order)
        return result

    def update_order(self, order, data):
        self.update_model_instance(order, **data)
        order = self.get_order(uuid=order.uuid)
        return order
