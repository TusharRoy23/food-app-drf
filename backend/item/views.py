from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from backend.common.pagination import BasePagination
from backend.common.views import BaseVisitorListAPIView, BaseVisitorRetrieveAPIView
from backend.rest_utils.exceptions import NotFoundException

from .config import ItemStatus
from .serializer import ItemOutputSerializer
from .services import ItemService


class ItemListAPIView(BaseVisitorListAPIView):
    service_class = ItemService
    output_serializer = ItemOutputSerializer
    pagination_class = BasePagination

    def list(self, request, *args, **kwargs):
        items = self.service_class(user=self.get_user()).list(
            **{"status": ItemStatus.ACTIVE}
        )
        paginated_items = self.paginate_queryset(items)
        if paginated_items is not None:
            output = self.output_serializer(paginated_items, many=True)
            return self.get_paginated_response(data=output.data)
        output = self.output_serializer(items, many=True)
        return Response(output.data)


class ItemRetrieveAPIView(BaseVisitorRetrieveAPIView):
    service_class = ItemService
    output_serializer = ItemOutputSerializer

    def get_object(self):
        try:
            obj = super().get_object(**{"status": ItemStatus.ACTIVE})
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFoundException("Item does not exist")
