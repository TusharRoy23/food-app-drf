from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models import BaseModel
from backend.restaurant.models import Restaurant

from ..common import ScreenMethodValidator
from ..item.models import Item
from .config import OrderStatus, PaidBy

User = get_user_model()


class Order(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="order_user",
        verbose_name="Order User",
        help_text=_("Order User"),
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="order_restaurant",
        verbose_name="Restaurant",
        help_text=_("The restaurant"),
    )
    order_amount = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        verbose_name="Order Amount",
        help_text=_("Only Order amount"),
    )
    total_amount = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        verbose_name="Total Amount",
        help_text=_("Total amount"),
    )
    rebate_amount = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        verbose_name="Rebate Amount",
        help_text=_("Rebate amount"),
    )
    status = models.CharField(
        choices=OrderStatus.CHOICES,
        default=OrderStatus.PENDING,
        verbose_name="status",
        help_text=_("Order Status"),
    )
    paid_by = models.CharField(
        choices=PaidBy.CHOICES,
        default=PaidBy.CASH_ON_DELIVERY,
        verbose_name="Paid By",
        help_text=_("Paid By"),
    )

    def __str__(self):
        return f"{self.uuid}-{self.user.username}"


class OrderItem(BaseModel):
    validators = [ScreenMethodValidator]
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name="orderitem_item",
        verbose_name="Order Item",
        help_text=_("Order Item"),
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name="orderitem_order",
        verbose_name="Order",
        help_text=_("Order"),
    )
    quantity = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Quantity",
        help_text=_("Order Item Quantity"),
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Item amount",
        help_text=_("Item Amount"),
    )
    total_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name="Total amount",
        help_text=_("Total Amount"),
    )
