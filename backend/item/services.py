from django.core.exceptions import ObjectDoesNotExist

from backend.common.services import BaseModelService
from backend.rest_utils.exceptions import NotFoundException

from .models import Item


class ItemService(BaseModelService):
    model = Item

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super(ItemService, self).__init__(user=user, *args, **kwargs)

    def create_item(self, **kwargs):
        kwargs["code"] = self.input_mixin.generate_unique_code("item")
        item = self.create(**kwargs)
        return item

    def get_items(self, **kwargs):
        return self.list(**kwargs)

    def get_item(self, **kwargs):
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist as ob:
            raise NotFoundException(message=str(ob))

    def update_item(self, item, **kwargs):
        return self.update_model_instance(item, **kwargs)
