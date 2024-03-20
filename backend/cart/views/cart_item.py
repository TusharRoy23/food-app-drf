from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response

from backend.cart.serializers import CartItemOutputSerializer
from backend.cart.serializers.cart_item import CartItemUpdateSerializer
from backend.cart.services.cart_item_service import CartItemService
from backend.common.views import BaseVisitorRetrieveUpdateDeleteAPIView
from backend.rest_utils.exceptions import NotFoundException


class CartItemUpdateDestroyView(BaseVisitorRetrieveUpdateDeleteAPIView):
    input_serializer = CartItemUpdateSerializer
    output_serializer = CartItemOutputSerializer
    service_class = CartItemService

    def get_object(self, **kwargs):
        try:
            obj = super().get_object()
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFoundException(message=_("Item not found"))

    def update(self, request, *args, **kwargs):
        cart_item = self.get_object()
        serializer = self.input_serializer(
            data=request.data, context={"cart_item": cart_item}
        )
        serializer.is_valid(raise_exception=True)
        result = self.service_class(user=self.get_user()).update_cart_item(
            serializer.validated_data
        )
        output = self.output_serializer(result)

        return Response(output.data)

    def delete(self, request, *args, **kwargs):
        cart_item = self.get_object()
        self.service_class(user=self.get_user()).delete_cart_item(cart_item)
        return Response(status=status.HTTP_204_NO_CONTENT)
