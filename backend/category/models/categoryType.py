from django.db import models

from backend.common.models import BaseModel


class CategoryType(BaseModel):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name