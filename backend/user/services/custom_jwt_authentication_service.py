from typing import Optional, Tuple

from rest_framework.request import Request
from rest_framework_simplejwt.authentication import AuthUser, JWTAuthentication
from rest_framework_simplejwt.tokens import Token

from .blacklist_token_service import TokenBlacklistService

"""
Doc for Custom JWT Authentication-
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html#rest_framework_simplejwt.authentication.JWTAuthentication
"""


class CustomJWTAuthenticationService(JWTAuthentication):

    def authenticate(self, request: Request) -> Optional[Tuple[AuthUser, Token]]:
        raw_token = self.get_raw_token_from_request(request)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        TokenBlacklistService.get_or_create_blacklisted_access_token(raw_token)
        user = self.get_user(
            validated_token
        )  # Return AuthUser using the validated token

        return user, validated_token

    def get_raw_token_from_request(
        self, request: Request
    ) -> bytes | None:  # use that python version <=3.10
        header = self.get_header(request)
        if header is None:
            return None

        raw_token = self.get_raw_token(
            header
        )  # Extract token from Authorization header
        if raw_token is None:
            return None

        return raw_token
