from typing import Any, Dict

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import (
    AuthUser,
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import Token

from .services.blacklist_token_service import TokenBlacklistService

User = get_user_model()


class CustomTokenObtainSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str | int]:
        try:
            user = User.objects.get(
                Q(email=attrs.get("username")) | Q(username=attrs.get("username"))
            )
            attrs["username"] = user.username
            data = super().validate(attrs)

            info = {
                "username": user.username,
                "name": f"{user.first_name} {user.last_name}",
                "email": user.email,
            }

            data["user"] = info  # noqa
            return data
        except User.DoesNotExist:
            msg = _("No active account found with the given credentials")
            raise AuthenticationFailed(msg, code="authorization")


class CustomRefreshTokenSerializer(TokenRefreshSerializer):
    access = serializers.CharField(required=True)

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        data["access"] = data.pop("access")
        data["refresh"] = data.pop("refresh")
        if attrs.get("access"):
            TokenBlacklistService.get_or_create_blacklisted_access_token(
                attrs["access"]
            )

        return data


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40)
    password = serializers.CharField(min_length=5, write_only=True)
    email = serializers.EmailField(max_length=40)
    confirm_password = serializers.CharField(min_length=5, write_only=True)
    is_visitor = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirm_password",
            "email",
            "first_name",
            "last_name",
            "is_visitor",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs.pop("confirm_password"):
            raise serializers.ValidationError({"password": _("Password did not match")})
        return attrs
