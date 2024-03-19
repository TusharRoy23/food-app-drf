from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response

from backend.common.views import (
    BaseRestaurantCreateListAPIView,
    BaseRestaurantRetrieveUpdateDestroyAPIView,
)
from backend.rest_utils.exceptions import NotFoundException

from .models import Item
from .serializer import ItemOutputSerializer, ItemSerializer, ItemUpdateSerializer
from .services import ItemService


class ItemListCreateView(BaseRestaurantCreateListAPIView):
    input_serializer = ItemSerializer
    output_serializer = ItemOutputSerializer
    service_class = ItemService

    def get_queryset(self):
        return Item.objects.filter(restaurant=self.get_restaurant_from_request().id)

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
            raise NotFoundException(message=str("item not found"))

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
