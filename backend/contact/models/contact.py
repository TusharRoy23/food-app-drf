from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models import BaseModel
from backend.restaurant.models import Restaurant

from .contact_group import ContactGroup


class Contact(BaseModel):
    restaurant = models.ForeignKey(
        Restaurant,
        related_name="contact_restaurant",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Restaurant"),
        help_text=_("For restaurant user"),
    )

    contact_group = models.ForeignKey(
        to=ContactGroup,
        related_name="contacts",
        on_delete=models.PROTECT,
        help_text=_("Contact Group"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.code}-{self.restaurant.name if self.restaurant else ''}"
