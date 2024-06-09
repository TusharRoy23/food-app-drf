from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from backend.order.models import Order


class OrderListFilter(FilterSet):
    keyword = CharFilter(method="filter_by_code")
    paid_by = CharFilter(method="filter_by_paid_by")
    status = CharFilter(method="filter_status")

    class Meta:
        model = Order
        fields = ["code", "paid_by", "status"]

    def filter_by_code(self, queryset, name, value):
        return queryset.filter(Q(code=value))

    def filter_by_paid_by(self, queryset, name, value):
        return queryset.filter(paid_by=value)

    def filter_status(self, queryset, name, value):
        return queryset.filter(status=value)
