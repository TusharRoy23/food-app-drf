from django.core.validators import MinValueValidator, MaxValueValidator
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
        default=1
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
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.PROTECT,
        verbose_name=_("Brand"),
        help_text=_("Select a Brand"),
        related_name="brand_items",
        default=1
    )
    sku = models.CharField(
        max_length=20,
        verbose_name=_("SKU"),
        help_text=_("Type a SKU"),
        null=True,
        blank=True,
    )
    image = models.TextField(
        verbose_name=_("Image"),
        help_text=_("set an image url"),
        null=True,
        blank=True,
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
        default=1
    )
    weight = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        default=1,
        verbose_name=_("Weight"),
        help_text=_("Ex. 1Kg, 1Packet, 1Box, etc. (Kg, Packet, and, Box are unit"),
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
        default=0
    )
    status = models.CharField(
        choices=ItemStatus.CHOICES,
        default=ItemStatus.ACTIVE,
        verbose_name=_("Item Status"),
        help_text=_("Select a Item Status"),
    )
    short_description = models.TextField(
        verbose_name=_("Short Description"),
        help_text=_("Set a Short Description"),
        null=True,
        blank=True,
        max_length=300
    )
    long_description = models.TextField(
        verbose_name=_("Long Description"),
        help_text=_("Set a Long Description"),
        null=True,
        blank=True,
    )
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.name} ({self.code})"
