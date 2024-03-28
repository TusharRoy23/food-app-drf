from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _

from backend.common import services
from backend.contact.services import (
    ContactGroupService,
    ContactPersonService,
    ContactService,
)
from backend.order.services import OrderService
from backend.rest_utils.exceptions import (
    BadRequestException,
    InvalidInputException,
    NotFoundException,
)
from backend.restaurant.models import Restaurant
from backend.user.services import UserService


class RestaurantService(services.BaseModelService):
    model = Restaurant

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()
        self.order_service = OrderService()
        self.contact_group_service = ContactGroupService()
        self.contact_service = ContactService()
        self.contact_person_service = ContactPersonService()

    def _create_contact(self, **kwargs):
        try:
            # Add Contact group - will change later for restaurant user
            contact_group = self.contact_group_service.get_info(code="restaurant_owner")
            # create contact
            contact = self.contact_service.register_contact(
                **{
                    "restaurant_id": kwargs["restaurant"].id,
                    "contact_group": contact_group,
                }
            )
            # create contact person
            contact_person = {
                "contact_id": contact.id,
                "user_id": kwargs["user"].id,
                "is_restaurant_owner": True,
                "is_restaurant_user": True,
            }
            self.contact_person_service.register_contact_person(**contact_person)
        except ValidationError as e:
            raise InvalidInputException(message=str(e))

    def register_restaurant(self, **kwargs):
        try:
            # check if the user exists
            email = kwargs.pop("email")
            user = self.user_service.get_user_info(email)

            contact_person = self.contact_person_service.get_contact_person(email)

            if user.is_visitor or contact_person is not None:
                raise BadRequestException(message=_("User already exists"))

            kwargs["code"] = self.input_mixin.generate_unique_code("res")
            restaurant = self.create(**kwargs)

            contact_data = {
                "restaurant": restaurant,
                "user": user,
            }
            self._create_contact(**contact_data)

            return restaurant
        except ValidationError as e:
            raise InvalidInputException(message=str(e))

    def get_restaurant_info(self, **kwargs):
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist as e:
            raise NotFoundException(message=str(e))

    def get_orders(self, **kwargs):
        return self.order_service.list(
            **{
                "restaurant": self.user.contact_person_user.contact.restaurant.id,
                **kwargs,
            }
        )

    def get_order(self, order_uuid):
        return self.order_service.get_order(
            **{
                "restaurant": self.user.contact_person_user.contact.restaurant.id,
                "uuid": order_uuid,
            }
        )

    def update_order(self, order, data):
        return self.order_service.update_order(order, data)
