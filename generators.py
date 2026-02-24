
import random
import string


def generate_email() -> str:
    prefix = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{prefix}@example.com"


def generate_password(length: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choices(alphabet, k=length))