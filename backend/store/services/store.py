from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _

from backend.common import services
from backend.contact.services import (
    ContactGroupService,
    ContactPersonService,
    ContactService,
)
from backend.order.models import Order
from backend.order.services import OrderService
from backend.rest_utils.exceptions import (
    BadRequestException,
    InvalidInputException,
    NotFoundException,
)
from backend.store.models import Store
from backend.user.services import UserService
from backend.user.services.user_notification_service import UserNotificationService


class StoreService(services.BaseModelService):
    model = Store

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()
        self.order_service = OrderService()
        self.contact_group_service = ContactGroupService()
        self.contact_service = ContactService()
        self.contact_person_service = ContactPersonService()

    def _create_contact(self, **kwargs):
        try:
            # Add Contact group - will change later for store user
            contact_group = self.contact_group_service.get_info(code="store_owner")
            # create contact
            contact = self.contact_service.register_contact(
                **{
                    "store_id": kwargs["store"].id,
                    "contact_group": contact_group,
                }
            )
            # create contact person
            contact_person = {
                "contact_id": contact.id,
                "user_id": kwargs["user"].id,
                "is_store_owner": True,
                "is_store_user": True,
            }
            self.contact_person_service.register_contact_person(**contact_person)
        except ValidationError as e:
            raise InvalidInputException(message=str(e))

    def __send_notification_to_user(self, order: Order):
        UserNotificationService(user_id=order.user.id).send_notification(
            **{"message": f"Order {order.code} is {order.status}"}
        )

    def register_store(self, **kwargs):
        try:
            # check if the user exists
            email = kwargs.pop("email")
            user = self.user_service.get_user_info(email)

            contact_person = self.contact_person_service.get_contact_person(email)

            if user.is_visitor or contact_person is not None:
                raise BadRequestException(message=_("User already exists"))

            kwargs["code"] = self.input_mixin.generate_unique_code("res")
            store = self.create(**kwargs)

            contact_data = {
                "store": store,
                "user": user,
            }
            self._create_contact(**contact_data)

            return store
        except ValidationError as e:
            raise InvalidInputException(message=str(e))

    def get_store_info(self, **kwargs):
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist as e:
            raise NotFoundException(message=str(e))

    def get_orders(self, **kwargs):
        return self.order_service.list(
            **{
                "store": self.user.contact_person_user.contact.store.id,
                **kwargs,
            }
        )

    def get_order(self, order_uuid):
        return self.order_service.get_order(
            **{
                "store": self.user.contact_person_user.contact.store.id,
                "uuid": order_uuid,
            }
        )

    def update_order(self, order, data):
        result = self.order_service.update_order(order, data)
        self.__send_notification_to_user(order)
        return result
