from django.urls import path

from . import views

app_name = "Item"
urlpatterns = [
    path("", views.ItemListAPIView.as_view(), name="item-list"),
    path(
        "<uuid:uuid>/",
        views.ItemRetrieveAPIView.as_view(),
        name="item-details",
    ),
]
