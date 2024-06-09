from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response

from backend.common.pagination import BasePagination
from backend.common.views import BaseVisitorListAPIView, BaseVisitorRetrieveAPIView
from backend.rest_utils.exceptions import NotFoundException

from .config import ItemStatus
from .filters import ItemListFilter
from .serializer import ItemOutputSerializer
from .services import ItemService


class ItemListAPIView(BaseVisitorListAPIView):
    service_class = ItemService
    output_serializer = ItemOutputSerializer
    pagination_class = BasePagination
    filterset_class = ItemListFilter

    def get_queryset(self):
        return self.service_class(user=self.request.user).get_items(**{"status": ItemStatus.ACTIVE})


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
