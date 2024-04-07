from django.contrib.auth import get_user_model
from django.urls import reverse
from factory.django import DjangoModelFactory
from rest_framework import status

from backend.common.tests.utils.custom_providers import Faker

User = get_user_model()


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    is_active = True
    is_staff = False
    is_superuser = False
    is_visitor = True

    class Meta:
        model = User


class JWTFactory:
    def __init__(self, client, user, password):
        self.jwt = None
        self.client = client
        self.user = user
        self.password = password
        self.url = reverse("user:login")
        self.__set_user_password()
        self.__generate_jwt()

    def get_jwt(self):
        return self.jwt

    def __set_user_password(self):
        self.user.set_password(self.password)
        self.user.save()

    def __generate_jwt(self):
        data = {"username": self.user.username, "password": self.password}
        response = self.client.post(self.url, data, format="json")

        if response.status_code == status.HTTP_200_OK:
            self.jwt = response.data["access"]

    def __str__(self):
        return self.jwt


# class TokenFactory:
#     def __init__(self, client, user, password):
#         self.token = None
#         self.client = client
#         self.user = user
#         self.username = self.user.username
#         self.password = password
#
#     def get_token(self):
#         return self.token
#
#     def __set_user_password(self):
#         self.user.set_password(self.password)
#         self.user.save()
#
#     def __generate_token(self):
#         token = Token
