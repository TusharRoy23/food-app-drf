from rest_framework import permissions, status
from rest_framework.response import Response

from backend.common.views import BaseCreateAPIView
from backend.store.services import StoreService

from ..serializers import RegisterStoreSerializer


class RegisterStoreView(BaseCreateAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    service_class = StoreService
    serializer_class = RegisterStoreSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        self.service_class().register_store(**serializer.validated_data)

        return Response(
            {"message": "Successfully Created.", "status": status.HTTP_201_CREATED}
        )
