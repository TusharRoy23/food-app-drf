import pytest

from backend.user.tests.factories import UserFactory


@pytest.fixture
def create_user():
    def _create_user(
        email: str,
        username: str,
        password: str = "recipe24@",
        is_active: bool = True,
        is_superuser: bool = False,
        is_staff: bool = False,
        is_visitor: bool = True,
    ):
        user = UserFactory.create(
            email=email,
            username=username,
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_visitor=is_visitor,
        )
        return user

    return _create_user
