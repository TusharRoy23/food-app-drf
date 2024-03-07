from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models.base import BaseModel
from backend.restaurant.models import Restaurant
from .config import ItemType, ItemStatus, MealType, MealState, MealFlavor


class Item(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        related_name='item_restaurant',
        on_delete=models.PROTECT,
        verbose_name=_('Restaurant'),
        help_text=_('Select a Restaurant')
    )
    name = models.CharField(max_length=20)
    item_type = models.CharField(
        choices=ItemType.CHOICES,
        default=ItemType.FOOD,
        verbose_name=_('Item Type'),
        help_text=_('Select a Item Type')
    )
    meal_type = models.CharField(
        choices=MealType.CHOICES,
        default=MealType.FASTFOOD,
        verbose_name=_('Meal Type'),
        help_text=_('Select a Meal Type')
    )
    meal_state = models.CharField(
        choices=MealState.CHOICES,
        default=MealState.HOT,
        verbose_name=_('Meal State'),
        help_text=_('Select a Meal State')
    )
    meal_flavor = models.CharField(
        choices=MealFlavor.CHOICES,
        default=MealFlavor.SWEET,
        verbose_name=_('Meal Flavor'),
        help_text=_('Select a Meal Flavor'),
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=15,
        verbose_name=_('Price of Item'),
        help_text=_('Set a Item Price'),
    )
    max_order_qty = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_('Max Order Qty'),
        help_text=_('Set a Max order Qty')
    )
    min_order_qty = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_('Min Order Qty'),
        help_text=_('Set a Min order Qty')
    )
    discount_rate = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name=_('Discount Rate'),
        help_text=_('Set a discount rate'),
    )
    status = models.CharField(
        choices=ItemStatus.CHOICES,
        default=ItemStatus.ACTIVE,
        verbose_name=_('Item Status'),
        help_text=_('Select a Item Status'),
    )


