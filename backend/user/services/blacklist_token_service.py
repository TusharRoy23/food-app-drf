from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.token_blacklist.models import (
    BlacklistedToken,
    OutstandingToken,
)
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.utils import datetime_from_epoch


class TokenBlacklistService:
    model = OutstandingToken

    @staticmethod
    def check_blacklisted_access_token(token):
        """
        Check if the token is blacklisted or not
        Yes: return invalid token
        No: pass
        AccessToken:
        https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html?
        highlight=AccessToken#module-rest_framework_simplejwt.tokens
        """
        access_token = AccessToken(token)
        if BlacklistedToken.objects.filter(token__jti=access_token["jti"]).exists():
            raise InvalidToken

    @staticmethod
    def get_or_create_outstanding_access_token(token):
        access_token = AccessToken(token)
        outstanding_access_token, is_created = OutstandingToken.objects.get_or_create(
            jti=access_token["jti"],
            defaults={
                "token": str(access_token),
                "expires_at": datetime_from_epoch(access_token["exp"]),
            },
        )

        return outstanding_access_token

    @staticmethod
    def get_or_create_blacklisted_access_token(token):
        outstanding_access_token = (
            TokenBlacklistService.get_or_create_outstanding_access_token(token)
        )
        BlacklistedToken.objects.get_or_create(token=outstanding_access_token)
