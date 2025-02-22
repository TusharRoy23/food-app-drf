from django.db import models
from backend.common.models import BaseModel


class Unit(BaseModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name