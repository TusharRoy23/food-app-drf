from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q

from backend.common.services import BaseModelService
from backend.contact.models import Contact
from backend.rest_utils.exceptions import InvalidInputException, NotFoundException


class ContactService(BaseModelService):
    model = Contact

    def __init__(self, *args, **kwargs):
        super(ContactService, self).__init__(*args, **kwargs)

    def register_contact(self, **kwargs):
        try:
            kwargs["code"] = self.input_mixin.generate_unique_code("con")
            return self.create(**kwargs)
        except ValidationError as e:
            raise InvalidInputException(message=str(e))

    def get_contact_info(self, keyword: str):
        try:
            return self.model.objects.get(Q(code=keyword))
        except ObjectDoesNotExist as ob:
            raise NotFoundException(message=str(ob))
