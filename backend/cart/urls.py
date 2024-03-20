from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path("", views.CartCreateAPIView.as_view(), name="cart-create"),
    path(
        "<uuid:uuid>/",
        views.CartRetrieveUpdateDestroyAPIView.as_view(),
        name="cart-retrieve-update",
    ),
    path(
        "<uuid:uuid>/cart-item/",
        views.CartItemUpdateDestroyView.as_view(),
        name="cart-item-update-delete",
    ),
]
