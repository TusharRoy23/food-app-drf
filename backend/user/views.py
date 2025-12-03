from django.db import IntegrityError
from django.conf import settings
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.common.views import BaseCreateAPIView
from backend.rest_utils.exceptions import InvalidInputException

from .serializers import (
    CustomRefreshTokenSerializer,
    CustomTokenObtainSerializer,
    RegisterUserSerializer,
)
from .services import UserService
from .tasks import send_email


class LoginUserView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        response = Response(serializer.validated_data, status=status.HTTP_200_OK)
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE_ACCESS'],  # e.g. 'access_token'
            value=serializer.validated_data['access'],
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=True,
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],  # 'Lax' or 'Strict'
            path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH']
        )
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE_REFRESH'],  # e.g. 'refresh_token'
            value=serializer.validated_data['refresh'],
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=True,
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            path=settings.SIMPLE_JWT['REFRESH_COOKIE_PATH']  # '/auth/refresh/' or '/'
        )

        # return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return response


class RefreshTokenView(TokenRefreshView):
    serializer_class = CustomRefreshTokenSerializer


class RegisterUserView(BaseCreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer
    service_class = UserService

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(
                data=request.data, context={"request": request}
            )
            serializer.is_valid(raise_exception=True)
            self.service_class().register_user(**serializer.validated_data)
            data = serializer.validated_data
            info = {
                "to_email": [data["email"]],
                "subject": "User registration",
                "body": f'Welcome Mr/Mrs {data["first_name"]} {data["last_name"]}',
            }
            send_email.delay(**info)
            return Response(
                {"msg": "Successfully Created.", "status": status.HTTP_201_CREATED}
            )
        except IntegrityError:
            raise InvalidInputException(
                message="Username or Email already exists",
                errors={"username": ["Username or Email already exists"]},
            )
