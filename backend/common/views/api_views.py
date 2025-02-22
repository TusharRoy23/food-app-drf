from rest_framework import generics

from backend.common.mixins import (
    IndividualVisitorAPIPermissionMixin,
    ListAPIMixin,
    RequestMixins,
    StoreAPIPermissionMixin,
    StoreStaffAPIPermissionMixin,
    RetrieveAPIMixin,
    VisitorAPIPermissionMixin,
)


class BaseGenericAPIView:
    """
    Common function and logic for all view
    """

    def get_serializer_class(self):
        if self.request.method == "GET" and hasattr(self, "output_serializer"):
            self.serializer_class = self.output_serializer
        elif hasattr(self, "input_serializer"):
            self.serializer_class = self.input_serializer

        return self.serializer_class

    def get_input_serializer(self, instance, **kwargs):
        if hasattr(self, "input_serializer"):
            return self.input_serializer(instance=instance, **kwargs)
        raise Exception("No Input serializer class set")

    def get_output_serializer(self, instance, **kwargs):
        if hasattr(self, "output_serializer"):
            return self.output_serializer(instance=instance, **kwargs)
        raise Exception("No Output serializer class set")


class BaseCreateAPIView(generics.CreateAPIView):
    """
    Base Create API View
    """

    service_class = None


class BaseCreateListAPIView(
    RequestMixins, BaseGenericAPIView, ListAPIMixin, generics.ListCreateAPIView
):
    """
    Base Create and List API View
    """

    service_class = None


class BaseListAPIView(
    RequestMixins, BaseGenericAPIView, ListAPIMixin, generics.ListAPIView
):
    """
    Base List API View
    """

    service_class = None


class BaseRetrieveAPIView(
    RequestMixins,
    RetrieveAPIMixin,
    BaseGenericAPIView,
    generics.RetrieveAPIView,
):
    """
    Base Retrieve API View
    """

    service_class = None


class BaseRetrieveUpdateDestroyAPIView(
    RequestMixins,
    RetrieveAPIMixin,
    BaseGenericAPIView,
    generics.RetrieveUpdateDestroyAPIView,
):
    """
    Base Update, Get and delete API View
    """

    service_class = None


class BaseStoreListAPIView(
    StoreAPIPermissionMixin,
    BaseListAPIView,
):
    """
    List permission for stores' users
    """


class BaseStoreCreateListAPIView(
    StoreAPIPermissionMixin, BaseCreateListAPIView
):
    """
    Create and Fetch permission for store users
    """


class BaseStoreRetrieveUpdateDestroyAPIView(
    StoreAPIPermissionMixin,
    StoreStaffAPIPermissionMixin,
    BaseRetrieveUpdateDestroyAPIView,
):
    """
    Fetch, Update and Delete permissions for store users
    """


class BaseVisitorAPIPermissionMixin(
    VisitorAPIPermissionMixin,
    IndividualVisitorAPIPermissionMixin,
):
    """
    Base permission mixin for Visitors
    """


class BaseVisitorCreateListAPIView(
    BaseVisitorAPIPermissionMixin,
    BaseCreateListAPIView,
):
    """
    Create, List permission for visitor users
    """


class BaseVisitorCreateAPIView(
    RequestMixins,
    BaseVisitorAPIPermissionMixin,
    BaseCreateAPIView,
):
    """
    Create permission for visitor users
    """


class BaseVisitorRetrieveUpdateDeleteAPIView(
    BaseVisitorAPIPermissionMixin,
    BaseRetrieveUpdateDestroyAPIView,
):
    """
    Fetch, Update and Delete permissions for visitor
    """


class BaseVisitorListAPIView(
    BaseVisitorAPIPermissionMixin,
    BaseListAPIView,
):
    """
    List permissions for visitor
    """


class BaseVisitorRetrieveAPIView(
    VisitorAPIPermissionMixin,
    BaseRetrieveAPIView,
):
    """
    Retrieve permissions for visitor
    """
