from django.urls import path

from . import views

app_name = "order"
urlpatterns = [
    path("", views.VisitorOrderCreateAPIView.as_view(), name="visitor-order-create")
]
