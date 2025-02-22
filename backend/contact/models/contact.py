from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models import BaseModel
from backend.store.models import Store

from .contact_group import ContactGroup


class Contact(BaseModel):
    store = models.ForeignKey(
        Store,
        related_name="contact_store",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Store"),
        help_text=_("For store user"),
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
        return f"{self.code}-{self.store.name if self.store else ''}"
