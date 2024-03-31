import random
import string
import uuid

from factory import Faker
from faker.providers import BaseProvider


class CustomFakerProvider(BaseProvider):
    def unique_code(self, length=8):
        chars = string.ascii_letters + string.digits
        code = "".join(random.choice(chars) for _ in range(length))
        return code

    def uuid(self):
        return str(uuid.uuid4())


Faker.add_provider(CustomFakerProvider)
