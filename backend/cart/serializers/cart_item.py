from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from backend.common.serializers import BaseSerializer
from backend.item.models import Item
from backend.item.serializer import BaseItemOutputSerializer
from backend.rest_utils.exceptions import InvalidInputException, NotFoundException

from ..models import CartItem


class CartItemCreateSerializer(BaseSerializer):
    uuid = serializers.UUIDField(required=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ["uuid", "quantity"]

    def validate(self, attrs):
        try:
            item_uuid = attrs.get("uuid")
            quantity = attrs.get("quantity")
            filter_kwargs = {"uuid": item_uuid}

            item = Item.objects.get(**filter_kwargs)
            if int(item.max_order_qty) != 0 and item.max_order_qty < quantity:
                raise InvalidInputException(
                    errors={"items": {"quantity": [_("order qty exceed")]}}
                )
            elif item.min_order_qty > quantity:
                raise InvalidInputException(
                    errors={"items": {"quantity": [_("order qty not met")]}}
                )
            attrs["item"] = item
            return attrs
        except ObjectDoesNotExist:
            raise NotFoundException(errors={"items": {"uuid": [_("Item not found")]}})


class CartItemOutputSerializer(BaseItemOutputSerializer):
    class Meta:
        model = CartItem
        fields = ["uuid", "quantity", "item", "amount", "total_amount"]


class CartItemUpdateSerializer(BaseSerializer):
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = CartItem
        fields = ["quantity"]

    def validate(self, attrs):
        quantity = attrs.get("quantity")
        cart_item = self.context.get("cart_item")
        if cart_item:
            if (
                int(cart_item.item.max_order_qty) != 0
                and cart_item.item.max_order_qty < quantity
            ):
                raise InvalidInputException(message=_("order qty exceed"))
            elif cart_item.item.min_order_qty > quantity:
                raise InvalidInputException(message=_("order qty not met"))

            attrs["cart_item"] = cart_item
            attrs["total_amount"] = round(cart_item.amount * quantity, 2)
        else:
            raise NotFoundException(message=_("item not found"))

        return attrs
