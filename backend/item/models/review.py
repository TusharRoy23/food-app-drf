from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from backend.common.models import BaseModel
from backend.contact.models import ContactPerson
from backend.item.models import Item


class Review(BaseModel):
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    comment = models.TextField(null=True,blank=True)
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='item_reviews',
        verbose_name='item',
    )
    contact_person = models.ForeignKey(
        ContactPerson,
        related_name='contact_person_reviews',
        verbose_name='Contact Person',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.item} - {self.rating}"