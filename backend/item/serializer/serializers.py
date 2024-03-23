from rest_framework import serializers

from backend.common.serializers import BaseSerializer, ExcludeFieldsMixin

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
