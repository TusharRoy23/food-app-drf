from rest_framework import serializers

from backend.common.serializers import BaseSerializer
from backend.item.serializer import BaseItemOutputSerializer
from backend.order.models import Order, OrderItem


class OrderCreateSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(required=True)

    class Meta:
        model = Order
        fields = ["uuid"]


class OrderItemOutputSerializer(BaseItemOutputSerializer):
    class Meta:
        model = OrderItem
        fields = ["uuid", "quantity", "item", "amount", "total_amount"]


class OrderOutputSerializer(BaseSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "uuid",
            "code",
            "order_amount",
            "total_amount",
            "rebate_amount",
            "paid_by",
            "items",
            "status",
            "created_at",
            "created_by",
        ]

    def get_items(self, order):
        serializer = OrderItemOutputSerializer(
            instance=OrderItem.objects.filter(order__uuid=order.uuid),
            many=True,
        )
        return serializer.data
