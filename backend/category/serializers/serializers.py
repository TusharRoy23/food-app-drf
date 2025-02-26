from rest_framework import serializers

from backend.category.models import Category
from backend.common.mixins import ExcludeFieldsMixin


class CategoryForVisitorOutputSerializer(ExcludeFieldsMixin, serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ["created_at", "updated_at", "created_by", "updated_by", "id"]

    def get_children(self, obj):
        return CategoryForVisitorOutputSerializer(obj.children, many=True, context=self.context).data
