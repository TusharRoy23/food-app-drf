from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q

from backend.common import services
from backend.contact.models import ContactPerson
from backend.rest_utils.exceptions import InvalidInputException


class ContactPersonService(services.BaseModelService):
    model = ContactPerson

    def register_contact_person(self, **kwargs):
        try:
            kwargs["code"] = self.input_mixin.generate_unique_code("per")
            return self.create(**kwargs)
        except ValidationError as e:
            raise InvalidInputException(message=str(e))

    def get_contact_person(self, keyword: str):
        try:
            return self.model.objects.get(
                Q(user__username=keyword) | Q(user__email=keyword)
            )
        except ObjectDoesNotExist:
            return None
