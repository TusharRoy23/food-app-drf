from django.contrib import admin

from .models import Cart, CartItem

class CartItemModelAdmin(admin.TabularInline):
    model = CartItem


class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemModelAdmin]

admin.site.register(Cart, CartModelAdmin)

