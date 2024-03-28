from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models import BaseModel, LogBaseModel


class DjangoContactGroup(LogBaseModel):
    contact_group = models.ForeignKey(
        to="ContactGroup",
        verbose_name=_("Contact Group"),
        help_text=_("Contact Group"),
        on_delete=models.CASCADE,
        related_name="contact_groups",
        related_query_name="contact_group",
    )
    django_group = models.ForeignKey(
        to=Group,
        verbose_name=_("Django Group"),
        help_text=_("Django Group"),
        on_delete=models.CASCADE,
        related_name="django_groups",
        related_query_name="django_group",
    )

    def __str__(self):
        return f"{self.contact_group} - {self.django_group}"


class ContactGroup(BaseModel):
    name = models.CharField(
        max_length=25,
        verbose_name=_("Name"),
        blank=True,
        help_text=_("Contact Group Name"),
    )
    django_groups = models.ManyToManyField(
        to=Group,
        verbose_name=_("Contact Group"),
        help_text=_("Contact Group"),
        blank=True,
        related_name="contact_groups",
        through_fields=("contact_group", "django_group"),
        through=DjangoContactGroup,
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
