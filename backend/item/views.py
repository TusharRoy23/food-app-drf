from django.core.exceptions import ObjectDoesNotExist

from backend.common.pagination import BasePagination
from backend.common.views import BaseListAPIView
from backend.common.views.api_views import BaseRetrieveAPIView
from backend.rest_utils.exceptions import NotFoundException
from rest_framework import permissions
from .config import ItemStatus
from .filters import ItemListFilter
from .serializer import ItemOutputSerializer
from .services import ItemService


class ItemListAPIView(BaseListAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    service_class = ItemService
    output_serializer = ItemOutputSerializer
    pagination_class = BasePagination
    filterset_class = ItemListFilter

    def get_queryset(self):
        return self.service_class(user=self.request.user).get_items(**{"status": ItemStatus.ACTIVE})


class ItemRetrieveAPIView(BaseRetrieveAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    service_class = ItemService
    output_serializer = ItemOutputSerializer

    def get_object(self):
        try:
            obj = super().get_object(**{"status": ItemStatus.ACTIVE})
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFoundException("Item does not exist")
