import json
import re
import uuid

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

"""
Customizing DB behaviour.
Ref: https://docs.djangoproject.com/en/4.2/topics/db/models/#overriding-predefined-model-methods
"""

User = get_user_model()


class AbstractBaseModel(models.Model):
    """This abstract model will be used by all the models"""

    class Meta:
        abstract = True

    validators = []

    def get_validators(self):
        """Return all the validators"""
        return self.validators

    def get_fields(self):
        """Return all the fields of objects/models"""
        fields = []

        # Appending all the fields & values of the objects/models
        for obj in self._meta.fields:  # noqa
            try:
                fields.append(getattr(self, obj.name))
            except ObjectDoesNotExist:
                pass

        return fields

    def get_screen_methods(self):
        """Return list of all methods which names' prefix is 'screen_'. Using it for checking some custom method in
        the model before saving to the DB"""

        screen_methods = []
        attributes = dir(self)
        pattern = re.compile("screen[_]*")
        for attribute in attributes:
            if pattern.match(attribute):
                screen_methods.append(getattr(self, attribute))

        return screen_methods

    def get_validate(self):
        """Pass the objects to all validators for validation"""

        validators = self.get_validators()
        for validator in validators:
            validator(obj=self).validate()

    def clean(self, *args, **kwargs):
        # Can also be written as super().clean()
        # ref: https://realpython.com/python-super/#a-super-deep-dive
        super(AbstractBaseModel, self).clean()
        self.get_validate()

    def save(self, *args, **kwargs):
        self.full_clean()  # this will execute the above clean function
        super(AbstractBaseModel, self).save(*args, **kwargs)

    def serialized_version(self, formats="json", fields=None):
        """Need to ask"""
        dumped = serialize(formats, [self], fields=fields)
        dumped = json.loads(dumped)
        serialized = dumped[0]["fields"]
        serialized["id"] = dumped[0]["pk"]
        return serialized


class LogBaseModel(AbstractBaseModel):
    """
    To keep the related_name unique for every child class -  use %{app_label} or %{class} or both.
    Ref: https://docs.djangoproject.com/en/4.2/topics/db/models/#be-careful-with-related-name-and-related-query-name
    """

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
        editable=False,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        abstract = True


class BaseModel(LogBaseModel):
    uuid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name=_("UUID"),
        help_text=_("Unique ID"),
    )
    code = models.CharField(max_length=120, help_text=_("Unique Code"), unique=True)

    class Meta:
        abstract = True


class BaseHistoryModel(BaseModel):
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
