from django.contrib import admin

from .models import Order, OrderItem


class OrderItemModelAdmin(admin.TabularInline):
    model = OrderItem


class OrderModelAdmin(admin.ModelAdmin):
    inlines = [OrderItemModelAdmin]


admin.site.register(Order, OrderModelAdmin)
