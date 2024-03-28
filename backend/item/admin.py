from django.contrib import admin

from .models import Item


class ItemAdminModel(admin.ModelAdmin):
    list_display = ("code", "name", "restaurant")


admin.site.register(Item, ItemAdminModel)
