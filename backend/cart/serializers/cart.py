from rest_framework import serializers

from backend.common.serializers import BaseSerializer

from ..models import Cart, CartItem
from .cart_item import CartItemCreateSerializer, CartItemOutputSerializer


class CartCreateSerializer(BaseSerializer):
    item = CartItemCreateSerializer(required=True)

    class Meta:
        model = Cart
        fields = ["item"]


class CartOutputSerializer(BaseSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            "uuid",
            "created_at",
            "cart_amount",
            "rebate_amount",
            "total_amount",
            "items",
        ]

    def get_items(self, cart):
        serializer = CartItemOutputSerializer(
            instance=CartItem.objects.filter(cart__uuid=cart.uuid),
            many=True,
        )
        return serializer.data
