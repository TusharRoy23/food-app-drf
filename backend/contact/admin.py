from django.contrib import admin

from .models import Contact, ContactPerson


class ContactPersonInline(admin.TabularInline):
    model = ContactPerson


class ContactModelAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    list_display = ["code", "restaurant", "created_at", "created_by"]
    inlines = [
        ContactPersonInline,
    ]


admin.site.register(Contact, ContactModelAdmin)
