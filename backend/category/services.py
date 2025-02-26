from backend.category.models import Category
from backend.common.services import BaseModelService


class CategoryService(BaseModelService):
    model = Category

    def __init__(self, user=None, *args, **kwargs):
        super(CategoryService, self).__init__(user=user,*args, **kwargs)

    def get_category_list(self):
        return Category.objects.filter(parent=None).prefetch_related('children')
