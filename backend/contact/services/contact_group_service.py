from backend.common.services import BaseModelService
from backend.contact.models import ContactGroup


class ContactGroupService(BaseModelService):
    model = ContactGroup

    def __init__(self, *args, **kwargs):
        super(ContactGroupService, self).__init__(*args, **kwargs)

    def get_info(self, **kwargs):
        return self.model.objects.get(**kwargs)
