from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User


class UserAdmin(auth_admin.UserAdmin):
    """
    Define the admin page for users.
    """
    ordering = ['id']
    search_fields = ['email', 'first_name', 'last_name']
    list_display = ['email', 'first_name', 'last_name', 'last_login', 'is_staff', 'is_superuser', 'is_active']
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (
            "Additional Permissions", {"fields": ("is_visitor", "is_restaurant_owner", "is_restaurant_user",)},
        ),
    )

    readonly_fields = ['last_login']
    add_fieldsets = fieldsets


admin.site.register(User, UserAdmin)
