from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from backend.common.pagination import BasePagination
from backend.common.views import BaseVisitorCreateListAPIView
from backend.order.serializers import OrderCreateSerializer, OrderOutputSerializer
from backend.order.services import OrderService
from backend.rest_utils.exceptions import NotFoundException

from ..filters import OrderListFilter


class VisitorOrderCreateAPIView(BaseVisitorCreateListAPIView):
    input_serializer = OrderCreateSerializer
    output_serializer = OrderOutputSerializer
    service_class = OrderService
    pagination_class = BasePagination
    filterset_class = OrderListFilter

    def list(self, request, *args, **kwargs):
        orders = (
            self.service_class()
            .list(
                **{"user_id": self.get_user().id, **request.query_params.dict()},
            )
            .order_by("-created_at")
        )
        orders = self.filter_queryset(orders)
        paginated_orders = self.paginate_queryset(orders)
        if paginated_orders is not None:
            output = self.get_serializer(paginated_orders, many=True)
            return self.get_paginated_response(output.data)
        output = self.output_serializer(orders, many=True)
        return Response(output.data)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.input_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            order = self.service_class(user=self.get_user()).create_order(
                serializer.validated_data
            )
            output = self.output_serializer(order)
            return Response(output.data)
        except ObjectDoesNotExist:
            raise NotFoundException(message=str("Not exist"))
