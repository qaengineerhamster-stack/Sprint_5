import random
import string


def generate_email(cohort: str = "1999", domain: str = "yandex.ru") -> str:
    suffix = "".join(random.choices(string.digits, k=3))
    return f"testtestov{cohort}{suffix}@{domain}"


def generate_password(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))