from django.urls import include, path

from . import views

app_name = "Restaurant"

item_patterns = (
    [
        path("", views.ItemListCreateView.as_view(), name="item-list"),
        path(
            "<uuid:uuid>/",
            views.ItemRetrieveUpdateDestroyAPIView.as_view(),
            name="item-details",
        ),
    ],
    "item",
)

order_patterns = (
    [
        path("", views.OrderListAPIView.as_view(), name="order-list"),
        path(
            "<uuid:uuid>/",
            views.OrderRetrieveUpdateAPIView.as_view(),
            name="order-details",
        ),
    ],
    "order",
)

urlpatterns = [
    path(
        "register/", views.RegisterRestaurantView.as_view(), name="register-restaurant"
    ),
    path("items/", include(item_patterns, namespace="item")),
    path("orders/", include(order_patterns, namespace="order")),
]
