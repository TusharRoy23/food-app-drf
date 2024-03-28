from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models import Q

from backend.common import services
from backend.contact.services import ContactPersonService, ContactService
from backend.rest_utils.exceptions import InvalidInputException, NotFoundException

User = get_user_model()


class UserService(services.BaseModelService):
    model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.contact_service = ContactService()
        self.contact_person_service = ContactPersonService()

    def __register_contact(self, **kwargs):
        contact = self.contact_service.get_contact_info(kwargs["contact_code"])

        contact_person = {
            "contact_id": contact.id,
            "user_id": kwargs["user"].id,
        }
        self.contact_person_service.register_contact_person(**contact_person)

    def register_user(self, **kwargs) -> User:
        try:
            user = self.create(**kwargs)
            user.set_password(kwargs["password"])
            user.save()

            if kwargs["is_visitor"]:
                kwargs["user"] = user
                kwargs["contact_code"] = "visitor"
                self.__register_contact(**kwargs)

            return user
        except ValidationError as ve:
            raise InvalidInputException(errors=ve)

    def get_user_info(self, keyword):
        try:
            return self.model.objects.get(Q(username=keyword) | Q(email=keyword))
        except ObjectDoesNotExist as e:
            raise NotFoundException(message=str(e))
