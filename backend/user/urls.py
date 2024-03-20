from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("register/", views.RegisterUserView.as_view(), name="register"),
    path("refresh-token/", views.RefreshTokenView.as_view(), name="refresh-token"),
]
