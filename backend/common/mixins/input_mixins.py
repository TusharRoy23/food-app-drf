import hashlib
import time


class InputMixins:
    @staticmethod
    def generate_unique_code(prefix: str) -> str:
        """
        This is a pure function that generates a unique string
        """
        timestamp = str(time.time())
        unq_str = hashlib.sha256((prefix + timestamp).encode()).hexdigest()
        return prefix + "-" + unq_str[-4:]
