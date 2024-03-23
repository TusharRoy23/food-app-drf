from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response

from backend.common.pagination import BasePagination
from backend.common.views import (
    BaseRestaurantListAPIView,
    BaseRetrieveUpdateDestroyAPIView,
)
from backend.order.serializers import OrderOutputSerializer
from backend.rest_utils.exceptions import NotFoundException

from ..serializers import OrderUpdateSerializer
from ..services import RestaurantService


class OrderListAPIView(BaseRestaurantListAPIView):
    output_serializer = OrderOutputSerializer
    service_class = RestaurantService
    pagination_class = BasePagination

    def list(self, request, *args, **kwargs):
        orders = self.service_class(user=self.get_user()).get_orders()
        paginated_orders = self.paginate_queryset(orders)
        if paginated_orders is not None:
            output = self.output_serializer(paginated_orders, many=True)
            return self.get_paginated_response(output.data)
        output = self.output_serializer(orders, many=True)
        return Response(data=output.data)


class OrderRetrieveUpdateAPIView(BaseRetrieveUpdateDestroyAPIView):
    input_serializer = OrderUpdateSerializer
    output_serializer = OrderOutputSerializer
    service_class = RestaurantService

    def get_object(self):
        try:
            uuid = self.kwargs["uuid"]
            return self.service_class(user=self.get_user()).get_order(order_uuid=uuid)
        except ObjectDoesNotExist:
            raise NotFoundException(message=_("Order does not exist"))

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        serializer = self.input_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.service_class(user=self.get_user()).update_order(
            order, serializer.validated_data
        )
        output = self.output_serializer(data)
        return Response(output.data, status=status.HTTP_200_OK)
