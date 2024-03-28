from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from backend.order.models import Order


class OrderListFilter(FilterSet):
    keyword = CharFilter(method="filter_by_code")

    class Meta:
        model = Order
        fields = ["code"]

    def filter_by_code(self, queryset, name, value):
        return queryset.filter(Q(code__icontains=value))
