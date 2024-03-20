from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from backend.cart.serializers import CartCreateSerializer, CartOutputSerializer
from backend.cart.services import CartService
from backend.common.views import (
    BaseVisitorCreateAPIView,
    BaseVisitorRetrieveUpdateDeleteAPIView,
)
from backend.rest_utils.exceptions import BadRequestException, NotFoundException


class CartCreateAPIView(BaseVisitorCreateAPIView):
    input_serializer = CartCreateSerializer
    output_serializer = CartOutputSerializer
    service_class = CartService

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.input_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = self.service_class(user=self.get_user()).create_cart(
                serializer.validated_data
            )
            output = self.output_serializer(result)
            return Response(output.data)
        except KeyError as e:
            raise BadRequestException(message=str(e))


class CartRetrieveUpdateDestroyAPIView(BaseVisitorRetrieveUpdateDeleteAPIView):
    input_serializer = CartCreateSerializer
    output_serializer = CartOutputSerializer
    service_class = CartService

    def get_object(self, **kwargs):
        try:
            obj = super().get_object()
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFoundException(message=str("No cart with uuid"))

    def update(self, request, *args, **kwargs):
        try:
            cart = self.get_object()
            serializer = self.input_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            result = self.service_class(user=self.get_user()).update_cart(
                cart, serializer.validated_data
            )
            output = self.output_serializer(result)
            return Response(output.data)
        except ObjectDoesNotExist:
            raise NotFoundException(message=str("No cart with uuid"))
