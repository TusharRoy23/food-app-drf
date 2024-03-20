from django.urls import path

from . import views

app_name = "Restaurant"
urlpatterns = [
    path(
        "register/", views.RegisterRestaurantView.as_view(), name="register-restaurant"
    )
]
