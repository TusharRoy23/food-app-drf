import json
import os

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import ContentType, Group, Permission
from django.test import RequestFactory
from rest_framework.test import APIClient, force_authenticate

from backend.user.tests.factories import JWTFactory, UserFactory

User = get_user_model()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture()
def request_factory() -> RequestFactory:
    return RequestFactory()


# @pytest.fixture
# def load_json_data():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     with open("".join([dir_path, '/fixtures/group.json'])) as json_file:
#         data = json.loads(json_file.read())
#     return data
#
# @pytest.fixture
# def load_permission_data():
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     with open("".join([dir_path, '/fixtures/permission.json'])) as json_file:
#         data = json.loads(json_file.read())
#     return data


@pytest.fixture
def client():
    headers = {"HTTP_POST": "localhost:8080"}
    return APIClient(**headers)


# @pytest.fixture
# def get_permissions(load_permission_data, load_json_data):
#     for data in load_json_data:
#         group = Group.objects.create(name=data['fields']['name'])
#         group.permissions.add(*data['fields']['permissions'])
#
# @pytest.fixture
# def get_groups(get_permissions):
#     def _get_groups(
#             is_store_user=False,
#             is_visitor=False,
#     ):
#         if is_store_user:
#             return Group.objects.filter(name="store-owner")
#         elif is_visitor:
#             return Group.objects.filter(name="visitors")
#         else:
#             return Group.objects.all()
#     return _get_groups


@pytest.fixture
def user():
    def _create_user(
        email: str,
        username: str,
        password: str = "recipe24@",
        is_active: bool = True,
        is_superuser: bool = True,
        is_staff: bool = False,
        is_visitor: bool = True,
    ):
        return UserFactory(
            email=email,
            username=username,
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_visitor=is_visitor,
        )

    return _create_user


@pytest.fixture
def login(user):
    def _do_login(email: str = "tushar@gm.com", username: str = "tushar"):
        return user(email, username)

    return _do_login


@pytest.fixture
def test_password():
    return "recipe24@"


@pytest.fixture
def jwt(client, user, test_password) -> JWTFactory:
    return JWTFactory(client, user, test_password)


@pytest.fixture
def auth_client(jwt, client):
    client.credentials(HTTP_AUTHORIZATION="Bearer {}".format(jwt))
    return client


@pytest.fixture
def force_auth(login):
    def _force_auth(request):
        return force_authenticate(request, user=login())

    return _force_auth
