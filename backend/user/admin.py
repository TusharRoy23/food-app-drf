from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(auth_admin.UserAdmin):
    """
    Define the admin page for users.
    """
    ordering = ['id']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_display = ['username', 'email', 'first_name', 'last_name', 'last_login', 'is_staff', 'is_superuser', 'is_active', 'is_visitor']
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (
            "Additional Info", {"fields": ("is_visitor",)},
        ),
    )

    readonly_fields = ['last_login']
    form = UserChangeForm
    add_form = UserCreationForm


admin.site.register(User, UserAdmin)
