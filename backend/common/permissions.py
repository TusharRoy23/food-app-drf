from rest_framework import permissions

from backend.rest_utils.exceptions import BadRequestException


class CustomDjangoModelPermission(permissions.DjangoModelPermissions):
    """
    This permission layer will fetch the 'service_class' from 'View'.
    A model class will available in service class. Based on that model
    API access will be determined by the CRUD of the model.

    Ref: https://github.com/encode/django-rest-framework/blob/master/rest_framework/permissions.py
    """

    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    def __model_from_service(self, view):
        """
        Get the model from service
        """
        assert getattr(view, "service_class", None) is not None, (
            "Cannot apply {} on view {} that does not set `service_class`"
        ).format(self.__class__.__name__, view)

        if not view.service_class.model:
            raise BadRequestException(
                message="'model' is missing for the service",
                errors="'model' is missing for the service",
            )
        return view.service_class.model

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, "_ignore_model_permissions", False):
            return True
        if not request.user or (
            not request.user.is_authenticated and self.authenticated_users_only
        ):
            return False

        model = self.__model_from_service(view)
        perms = self.get_required_permissions(request.method, model)

        return request.user.has_perms(perms)


class IsRestaurantUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user
            and not request.user.is_anonymous
            and request.user.contact_person_user.is_restaurant_user
        )


class IsRestaurantStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.contact_person_user.contact.restaurant.id == obj.restaurant.id
        )


class IsVisitorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and not request.user.is_anonymous and request.user.is_visitor
        )


class IsIndividualVisitorUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if type(obj).__name__ == "CartItem":
            user_id = obj.cart.user.id
        else:
            user_id = obj.user.id

        return bool(request.user.id == user_id)
