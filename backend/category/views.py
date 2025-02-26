from rest_framework import permissions
from backend.category.serializers import CategoryForVisitorOutputSerializer
from backend.category.services import CategoryService
from backend.common.views import BaseListAPIView


class CategoryListViewForVisitor(BaseListAPIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    service_class = CategoryService
    serializer_class = CategoryForVisitorOutputSerializer

    def get_queryset(self):
        return self.service_class().get_category_list()
