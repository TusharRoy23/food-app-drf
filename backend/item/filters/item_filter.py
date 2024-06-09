from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from backend.item.models import Item


class ItemListFilter(FilterSet):
    keyword = CharFilter(method="filter_by_name_or_code")
    item_type = CharFilter(method="filter_by_item_type")
    meal_type = CharFilter(method="filter_by_meal_type")
    meal_state = CharFilter(method="filter_by_meal_state")
    meal_flavor = CharFilter(method="filter_by_meal_flavor")

    class Meta:
        model = Item
        fields = ["name", "code", 'item_type', 'meal_type', 'meal_state', 'meal_flavor']

    def filter_by_name_or_code(self, queryset, name, value):
        return queryset.filter(Q(code=value) | Q(name__icontains=value))

    def filter_by_item_type(self, queryset, name, value):
        return queryset.filter(item_type=value)

    def filter_by_meal_type(self, queryset, name, value):
        return queryset.filter(meal_type=value)

    def filter_by_meal_state(self, queryset, name, value):
        return queryset.filter(meal_state=value)

    def filter_by_meal_flavor(self, queryset, name, value):
        return queryset.filter(meal_flavor=value)
