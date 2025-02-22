from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models.base import BaseModel
from backend.store.models import Store

from ..config import ItemStatus, ItemFlavor, ItemState


class Item(BaseModel):
    store = models.ForeignKey(
        Store,
        related_name="store_items",
        on_delete=models.PROTECT,
        verbose_name=_("Store"),
        help_text=_("Select a Store"),
    )
    name = models.CharField(max_length=20)
    category = models.ForeignKey(
        "category.Category",
        on_delete=models.PROTECT,
        verbose_name=_("Category"),
        help_text=_("Select a Category"),
        related_name="category_items",
        default=1
    )
    item_type = models.ForeignKey(
        "ItemType",
        on_delete=models.PROTECT,
        verbose_name=_("Item Type"),
        help_text=_("Select a Item Type"),
        related_name="item_type_items",
    )
    item_state = models.CharField(
        choices=ItemState.CHOICES,
        default=ItemState.NORMAL,
        verbose_name=_("Item State"),
        help_text=_("Select a Item State"),
    )
    item_flavor = models.CharField(
        choices=ItemFlavor.CHOICES,
        default=ItemFlavor.NONE,
        verbose_name=_("Item Flavor"),
        help_text=_("Select a Item Flavor"),
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=15,
        verbose_name=_("Price of Item"),
        help_text=_("Set a Item Price"),
    )
    max_order_qty = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Max Order Qty"),
        help_text=_("Set a Max order Qty"),
    )
    min_order_qty = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Min Order Qty"),
        help_text=_("Set a Min order Qty"),
    )
    unit = models.ForeignKey(
        "Unit",
        on_delete=models.PROTECT,
        verbose_name=_("Unit"),
        help_text=_("Select a Unit"),
        related_name="+",
    )
    discount_rate = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_("Discount Rate"),
        help_text=_("Set a discount rate"),
    )
    status = models.CharField(
        choices=ItemStatus.CHOICES,
        default=ItemStatus.ACTIVE,
        verbose_name=_("Item Status"),
        help_text=_("Select a Item Status"),
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
