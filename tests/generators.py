import random
import string
from datetime import datetime


def generate_email(name: str, surname: str, cohort: int, domain: str = "yandex.ru") -> str:
    # Формат по ТЗ: имя_фамилия_номерКогорты_любые3цифры@домен
    suffix3 = random.randint(100, 999)
    time_tail = datetime.now().strftime("%H%M%S")
    return f"{name}_{surname}_{cohort}_{suffix3}{time_tail}@{domain}".lower()


def generate_password(length: int = 8) -> str:
    # Минимум 6 символов
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(max(length, 6)))