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

    def price(self, length=3):
        min_value = 10 ** (length - 1)
        max_value = (10**length) - 1
        return random.randint(min_value, max_value)

    def food(self):
        foods = ["rice", "daal", "fish", "yam", "beans", "spaghetti"]
        return self.random_element(foods)


Faker.add_provider(CustomFakerProvider)
