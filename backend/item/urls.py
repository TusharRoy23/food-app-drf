from django.urls import path

from . import views

app_name = "Item"
urlpatterns = [
    path("", views.ItemListCreateView.as_view(), name="item-list"),
    path(
        "details/<uuid:uuid>/",
        views.ItemRetrieveUpdateDestroyAPIView.as_view(),
        name="item-details",
    ),
]
