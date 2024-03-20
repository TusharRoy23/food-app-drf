from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models.base import BaseModel
from backend.rest_utils.exceptions import InvalidInputException
from backend.restaurant.models import Restaurant

User = get_user_model()


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

    def __str__(self):
        return f"{self.code}-{self.restaurant.name if self.restaurant else ''}"


class ContactPerson(BaseModel):
    contact = models.ForeignKey(
        Contact,
        related_name="contact_person_contact",
        on_delete=models.PROTECT,
        verbose_name=_("Contact"),
        help_text=_("Contact for person"),
    )
    user = models.OneToOneField(
        User,
        related_name="contact_person_user",
        on_delete=models.PROTECT,
        verbose_name=_("User"),
        help_text=_("Contact person user"),
    )
    address = models.CharField(
        max_length=120,
        default=None,
        null=True,
        blank=True,
        verbose_name=_("Contact Person address"),
    )
    is_restaurant_owner = models.BooleanField(default=False)
    is_restaurant_user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email}-{self.contact.restaurant.name if self.contact.restaurant else ''}"

    def screen_contact_person(self):
        if (
            self.is_restaurant_user or self.is_restaurant_owner
        ) and self.contact.restaurant is None:
            raise InvalidInputException(message="Restaurant is required")
