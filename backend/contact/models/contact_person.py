from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models import BaseModel

from ...rest_utils.exceptions import InvalidInputException
from .contact import Contact

User = get_user_model()


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
        verbose_name=_("Contact Person address"),
    )
    mobile = models.CharField(
        max_length=12,
        verbose_name=_("mobile number"),
        null=True,
        blank=True
    )
    country = models.CharField(
        max_length=20,
        verbose_name=_("Country")
    )
    state = models.CharField(
        max_length=50,
        verbose_name=_("State")
    )
    city = models.CharField(
        max_length=20,
        verbose_name=_("City")
    )
    postal_code = models.CharField(
        max_length=10,
        verbose_name=_("Postal Code")
    )
    is_store_owner = models.BooleanField(default=False)
    is_store_user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email}-{self.contact.store.name if self.contact.store else ''}"

    def screen_contact_person(self):
        if (
            self.is_store_user or self.is_store_owner
        ) and self.contact.store is None:
            raise InvalidInputException(message="Store is required")
