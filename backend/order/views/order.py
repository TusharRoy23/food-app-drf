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
