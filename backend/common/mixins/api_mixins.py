import re

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from backend.common.permissions import (
    IsIndividualVisitorUser,
    IsStoreStaff,
    IsStoreUser,
    IsVisitorUser,
)


class RetrieveAPIMixin(object):
    def get_object(self, **queryset):
        """
        This method will override the 'get_object' method of 'GenericAPiView' class of DRF.
        :return: model instance
        """
        assert self.service_class is not None, (
            "'%s' should either include a 'service_class' attribute, "
            "or override the 'get_object()' method. " % self.__class__.__name__
        )

        query_params = {}
        if queryset:
            query_params.update(queryset)
        service = self.service_class(user=self.request.user)

        uuid = self.kwargs.get("uuid")
        return service.read_by_uuid(uuid, **query_params)


class ListAPIMixin(object):
    def __prepare_query_params_dict(self):
        valid_query_string_pattern = re.compile(r"^[\w\- .,]+$")
        query_params_dict = self.request.query_params.dict()
        # TODO: will add more in the future

        for key, value in query_params_dict.items():
            if valid_query_string_pattern.match(str(value)) is None:
                raise ValidationError({"detail": ["Invalid query"]})

        return query_params_dict

    def get_queryset(self, **kwargs):
        """
        This method will override the 'get_queryset' method of 'GenericAPiView' class of DRF.
        :return: queryset instance
        """
        assert self.service_class is not None, (
            "'%s' should either include a 'service_class' attribute, "
            "or override the 'get_queryset()' method." % self.__class__.__name__
        )
        query_params_dict = self.__prepare_query_params_dict()
        user = self.request.user
        service = self.service_class(user=user)

        if kwargs is not None:
            query_params_dict.update(kwargs)

        return service.list(**query_params_dict)

    def list(self, request, *args, **kwargs):
        """
        This is default method for view to get the list of a Model.
        meaning: Can use this without explicitly defining list() method
        """
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(
                page, many=True, context={"request": request}
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class StoreAPIPermissionMixin:

    def get_permissions(self):
        """
        Return the list of permission that the subclassed view required
        :permission: Is store User?
        """
        permissions = super().get_permissions()
        permissions.append(IsStoreUser())

        return permissions


class StoreStaffAPIPermissionMixin:
    def get_permissions(self):
        """
        Return the list of permission that the subclassed view required
        :permission: Is this store's staff?
        """
        permissions = super().get_permissions()
        permissions.append(IsStoreStaff())

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
