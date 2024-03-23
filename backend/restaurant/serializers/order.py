from rest_framework import serializers

from backend.order.config import OrderStatus
from backend.order.models import Order


class OrderUpdateSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=OrderStatus.CHOICES)

    class Meta:
        model = Order
        fields = ["status"]

    # def get_status(self, order):
    #     return
