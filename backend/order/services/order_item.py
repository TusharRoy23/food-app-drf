from django.db.models import Sum

from backend.common.services import BaseModelService
from backend.order.models import OrderItem

from ..config import OrderStatus


class OrderItemService(BaseModelService):
    model = OrderItem

    def __init__(self, user=None, *args, **kwargs):
        super(OrderItemService, self).__init__(user=user, *args, **kwargs)

    def __update_order(self, order):
        from .order import OrderService

        self.order_service = OrderService(user=self.user)

        total_amount = self.model.objects.filter(order__id=order.id).aggregate(
            total_amount=Sum("total_amount")
        )["total_amount"]
        return self.order_service.update_order(
            order,
            {"total_amount": total_amount, "order_status": OrderStatus.IN_PROGRESS},
        )

    def create_order_item(self, order, cart_items):
        for cart_item in cart_items:
            self.create(
                code="odr-itm-",
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity,
                amount=cart_item.amount,
                total_amount=cart_item.total_amount,
            )

        return self.__update_order(order)
