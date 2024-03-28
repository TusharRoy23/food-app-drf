from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from backend.item.models import Item


class ItemListFilter(FilterSet):
    keyword = CharFilter(method="filter_by_name_or_code")

    class Meta:
        model = Item
        fields = ["name", "code"]

    def filter_by_name_or_code(self, queryset, name, value):
        return queryset.filter(Q(code__icontains=value) | Q(name__icontains=value))
