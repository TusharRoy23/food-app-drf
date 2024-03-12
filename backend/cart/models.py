from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from backend.restaurant.models import Restaurant
from backend.common.models import BaseModel
from backend.item.models import Item
from backend.common.validators import ScreenMethodValidator
from .config import CartStatus

User = get_user_model()


class Cart(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='cart_user',
        verbose_name='Cart User',
        help_text=_('Cart User')
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='cart_restaurant',
        verbose_name='Restaurant',
        help_text=_('The restaurant'),
    )
    cart_amount = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        verbose_name='Cart Amount',
        help_text=_('Only Cart amount'),
    )
    total_amount = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        verbose_name='Total Amount',
        help_text=_('Total amount'),
    )
    rebate_amount = models.DecimalField(
        default=0.0,
        max_digits=10,
        decimal_places=2,
        verbose_name='Rebate Amount',
        help_text=_('Rebate amount'),
    )
    status = models.CharField(
        choices=CartStatus.CHOICES,
        default=CartStatus.SAVED,
        verbose_name='status',
        help_text=_('Cart Status')
    )

    def __str__(self):
        return f'{self.uuid}'


class CartItem(BaseModel):
    validators = [ScreenMethodValidator]
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name='cartitem_item',
        verbose_name='Cart Item',
        help_text=_('Cart Item'),
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.PROTECT,
        related_name='cartitem_cart',
        verbose_name='Cart',
        help_text=_('Cart')
    )
    quantity = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name='Quantity',
        help_text=_('Cart Item Quantity'),
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name='Item amount',
        help_text=_('Item Amount'),
    )
    total_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name='Total amount',
        help_text=_('Total Amount'),
    )

    def screen_item_quantity_check(self):
        item = Item.objects.get(uuid=self.item.uuid)
        # if item.quantity <=
