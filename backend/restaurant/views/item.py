from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response

from backend.common.pagination import BasePagination
from backend.common.views import (
    BaseRestaurantCreateListAPIView,
    BaseRestaurantRetrieveUpdateDestroyAPIView,
)
from backend.item.filters import ItemListFilter
from backend.item.serializer import ItemOutputSerializer
from backend.item.services import ItemService
from backend.rest_utils.exceptions import NotFoundException

from ..serializers import ItemSerializer, ItemUpdateSerializer


class ItemListCreateView(BaseRestaurantCreateListAPIView):
    input_serializer = ItemSerializer
    output_serializer = ItemOutputSerializer
    service_class = ItemService
    pagination_class = BasePagination
    filterset_class = ItemListFilter

    def list(self, request, *args, **kwargs):
        items = self.get_queryset(
            **{"restaurant__id": self.get_restaurant_from_request().id}
        ).order_by("-created_at")
        items = self.filter_queryset(items)
        paginated_items = self.paginate_queryset(items)
        if paginated_items is not None:
            output = self.output_serializer(paginated_items, many=True)
            return self.get_paginated_response(output.data)
        output = self.output_serializer(items, many=True)
        return Response(output.data)

    def post(self, request, *args, **kwargs):
        serializer = self.input_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["restaurant_id"] = (
            self.get_restaurant_from_request().id
        )
        self.service_class(user=self.get_user()).create_item(
            **serializer.validated_data
        )
        return Response(
            {"msg": "Successfully Created.", "status": status.HTTP_201_CREATED}
        )


class ItemRetrieveUpdateDestroyAPIView(BaseRestaurantRetrieveUpdateDestroyAPIView):
    service_class = ItemService
    input_serializer = ItemUpdateSerializer
    output_serializer = ItemOutputSerializer

    def get_object(self):
        try:
            obj = super().get_object()
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFoundException(message=str("Item does not exist"))

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.input_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        item = self.service_class(user=self.get_user()).update_item(
            item, **serializer.validated_data
        )
        output = self.output_serializer(item)
        return Response(output.data)
