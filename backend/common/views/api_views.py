from rest_framework import generics

from backend.common.mixins import (
    IndividualVisitorAPIPermissionMixin,
    RequestMixins,
    RestaurantAPIPermissionMixin,
    RestaurantStaffAPIPermissionMixin,
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
    RequestMixins, BaseGenericAPIView, generics.ListCreateAPIView
):
    """
    Base Create and List API View
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


class BaseRestaurantCreateListAPIView(
    RestaurantAPIPermissionMixin, BaseCreateListAPIView
):
    """
    Create and Fetch permission for restaurant users
    """


class BaseRestaurantRetrieveUpdateDestroyAPIView(
    RestaurantAPIPermissionMixin,
    RestaurantStaffAPIPermissionMixin,
    BaseRetrieveUpdateDestroyAPIView,
):
    """
    Fetch, Update and Delete permissions for restaurant users
    """


class BaseVisitorAPIView(
    VisitorAPIPermissionMixin,
    IndividualVisitorAPIPermissionMixin,
):
    """
    Base View for Visitors
    """


class BaseVisitorCreateAPIView(
    RequestMixins,
    BaseVisitorAPIView,
    BaseCreateAPIView,
):
    """
    Create permission for visitor users
    """


class BaseVisitorRetrieveUpdateDeleteAPIView(
    BaseVisitorAPIView,
    BaseRetrieveUpdateDestroyAPIView,
):
    """
    Fetch, Update and Delete permissions for visitor
    """
