from rest_framework import serializers

from backend.item.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["restaurant", "code"]


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["id", "restaurant", "code"]
