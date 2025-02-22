from django.contrib import admin

from .models import Store


class StoreModelAdmin(admin.ModelAdmin):
    ordering = ['-created_at']
    list_display = ['name', 'status', 'created_at', 'created_by']


admin.site.register(Store, StoreModelAdmin)
