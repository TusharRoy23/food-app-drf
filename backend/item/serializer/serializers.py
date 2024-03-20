from rest_framework import serializers

from backend.common.serializers import BaseSerializer, ExcludeFieldsMixin

from ..models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["restaurant", "code"]


class ItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ["id", "restaurant", "code"]


class ItemOutputSerializer(ExcludeFieldsMixin, BaseSerializer):
    class Meta:
        model = Item
        exclude = ["id", "restaurant"]
