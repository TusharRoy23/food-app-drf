from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

from backend.contact.models import ContactPerson
from backend.rest_utils.exceptions import BadRequestException


class ChannelJwtAuthMiddleware(BaseMiddleware):
    """
    Middleware for WS auth
    """

    async def __call__(self, scope, receive, send):
        try:
            jwt_value = None
            for key, value in scope.get("headers", []):
                if key.decode() == "token":
                    jwt_value = value
                    break
            user = await self.validate_token(jwt_value)
            if user:
                scope["contact_person"] = await self.get_contact_person(user)
        except (InvalidToken, TokenError, ValueError):
            scope["contact_person"] = None

        return await super().__call__(scope, receive, send)

    @database_sync_to_async
    def validate_token(self, token):
        try:
            jwt_authentication = JWTAuthentication()
            validated_token = jwt_authentication.get_validated_token(token)
            return jwt_authentication.get_user(validated_token)
        except BadRequestException:
            return None

    @database_sync_to_async
    def get_contact_person(self, user):
        try:
            data = ContactPerson.objects.get(user__id=user.id)
            return dict(
                {
                    "store_code": (
                        data.contact.store.code
                        if data.contact.store
                        else None
                    ),
                    "user_id": data.user.id,
                    "is_store_user": data.is_store_user,
                }
            )
        except ObjectDoesNotExist:
            return None
