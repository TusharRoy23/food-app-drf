from django.db import models
from backend.common.models import BaseModel


class Brand(BaseModel):
    name = models.CharField(unique=True, max_length=50)
    image= models.TextField(null=True, blank=True)
    logo = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - ({self.code})"