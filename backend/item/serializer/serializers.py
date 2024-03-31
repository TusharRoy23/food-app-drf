from rest_framework import serializers

from backend.common.mixins import ExcludeFieldsMixin
from backend.common.serializers import BaseSerializer

from ..models import Item


class ItemOutputSerializer(ExcludeFieldsMixin, BaseSerializer):
    class Meta:
        model = Item
        exclude = ["id", "restaurant"]


class BaseItemOutputSerializer(BaseSerializer):
    item = serializers.SerializerMethodField()

    def get_item(self, model):
        serializer = ItemOutputSerializer(
            instance=Item.objects.get(uuid=model.item.uuid),
            fields=["uuid", "name", "code"],
        )
        return serializer.data
