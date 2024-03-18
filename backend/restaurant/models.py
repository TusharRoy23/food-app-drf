from django.db import models
from django.utils.translation import gettext_lazy as _

from backend.common.models import BaseModel
from .config import CurrentStatus


class Restaurant(BaseModel):
    name = models.CharField(
        max_length=15,
        verbose_name=_('Restaurant'),
        help_text=_("Name of the Restaurant"),
    )
    address = models.CharField(
        max_length=100,
        verbose_name=_('Address'),
        help_text=_('Restaurant Address')
    )
    picture = models.URLField(
        default=None,
        blank=True,
        null=True,
        verbose_name=_('Profile picture URL'),
        help_text=_('URL of profile picture')
    )
    opening_time = models.TimeField(
        blank=False,
        null=False,
        verbose_name=_('Opening time'),
        help_text=_('Opening time')
    )
    closing_time = models.TimeField(
        blank=False,
        null=False,
        verbose_name=_('Closing time'),
        help_text=_('Closing time')
    )
    status = models.CharField(
        choices=CurrentStatus.CHOICES,
        default=CurrentStatus.NOT_VERIFIED,
        verbose_name=_('status'),
        help_text=_('Restaurant status')
    )

    def __str__(self):
        return f"{self.name}"



