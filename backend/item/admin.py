from django.contrib import admin

from .models import Item, ItemType, Unit


class ItemAdminModel(admin.ModelAdmin):
    list_display = ("code", "name", "store")


admin.site.register(Item, ItemAdminModel)
admin.site.register(ItemType)
admin.site.register(Unit)
