from backend.common.permissions import (
    IsIndividualVisitorUser,
    IsRestaurantStaff,
    IsRestaurantUser,
    IsVisitorUser,
)


class RetrieveAPIMixin(object):
    def get_object(self):
        """
        This method will override the 'get_object' method of 'GenericAPiView' class of DRF.
        :return: model instance
        """
        assert self.service_class is not None, (
            "'%s' should either include a 'service_class' attribute, "
            "or override the 'get_object()' method. " % self.__class__.__name__
        )

        query_params = {}
        service = self.service_class(user=self.request.user)

        uuid = self.kwargs.get("uuid")
        return service.read_by_uuid(uuid, **query_params)


class RestaurantAPIPermissionMixin:

    def get_permissions(self):
        """
        Return the list of permission that the subclassed view required
        :permission: Is restaurant User?
        """
        permissions = super().get_permissions()
        permissions.append(IsRestaurantUser())

        return permissions


class RestaurantStaffAPIPermissionMixin:
    def get_permissions(self):
        """
        Return the list of permission that the subclassed view required
        :permission: Is this restaurant's staff?
        """
        permissions = super().get_permissions()
        permissions.append(IsRestaurantStaff())

        return permissions


class VisitorAPIPermissionMixin:
    def get_permissions(self):
        """
        Return the list of permission that the subclassed view required
        :premission: Is this visitor?
        """
        permissions = super().get_permissions()
        permissions.append(IsVisitorUser())

        return permissions


class IndividualVisitorAPIPermissionMixin:
    def get_permissions(self):
        """
        Return the list of permission that the subclassed view required
        :premission: Is this individual visitor user?
        """
        permissions = super().get_permissions()
        permissions.append(IsIndividualVisitorUser())

        return permissions
