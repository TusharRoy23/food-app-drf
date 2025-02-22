from django.db import models
from django.utils.translation import gettext_lazy as _
from backend.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=25, unique=True)
    icon = models.TextField(
        null=True,
        blank=True,
        help_text=_("only fab icons")
    )
    discount = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        help_text=_("Discount for this category's Items"),
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        help_text=_("Parent Category"),
    )
    category_type = models.ForeignKey(
        'CategoryType',
        on_delete=models.CASCADE,
        help_text=_("Category Type"),
        default=1,
        related_name='categories',
    )

    def __str__(self):
        return f"{self.code}-{self.name}"