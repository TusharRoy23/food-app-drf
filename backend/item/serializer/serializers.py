from rest_framework import serializers

from backend.common.mixins import ExcludeFieldsMixin
from backend.common.serializers import BaseSerializer, ExcludeLogSerializer

from ..models import Item, Brand, ItemType, Unit
from ...category.serializers import CategoryForVisitorOutputSerializer


class BrandOutputSerializer(ExcludeFieldsMixin, BaseSerializer):
    class Meta:
        model = Brand
        exclude = ["id"]

class ItemTypeOutputSerializer(ExcludeFieldsMixin, BaseSerializer):
    class Meta:
        model = ItemType
        exclude = ["id"]

class UnitOutputSerializer(ExcludeFieldsMixin, BaseSerializer):
    class Meta:
        model = Unit
        exclude = ["id"]

class ItemOutputSerializer(ExcludeFieldsMixin, ExcludeLogSerializer):
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    item_type = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()

    class Meta:
        model = Item
        exclude = ExcludeLogSerializer.Meta.exclude + ["store"]

    def get_category(self, obj):
        serializer = CategoryForVisitorOutputSerializer(
            instance=obj.category,
            fields=["uuid", "name", "code"]
        )
        return serializer.data

    def get_brand(self, obj):
        serializer = BrandOutputSerializer(
            instance=obj.brand,
            fields=["uuid", "name", "code"]
        )
        return serializer.data

    def get_item_type(self, obj):
        serializer = ItemTypeOutputSerializer(
            instance=obj.item_type,
            fields=["uuid", "name", "code"]
        )
        return serializer.data

    def get_unit(self, obj):
        serializer = UnitOutputSerializer(
            instance=obj.unit,
            fields=["uuid", "name", "code"]
        )
        return serializer.data


class BaseItemOutputSerializer(BaseSerializer):
    item = serializers.SerializerMethodField()

    def get_item(self, model):
        serializer = ItemOutputSerializer(
            instance=Item.objects.get(uuid=model.item.uuid),
            fields=["uuid", "name", "code"],
        )
        return serializer.data