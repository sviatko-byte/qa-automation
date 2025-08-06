import os
import time
import random
import string

def is_file_downloaded(file_path, timeout=10):
    """
    Чекає до `timeout` секунд, щоб перевірити, чи файл з'явився.
    :param file_path: повний шлях до очікуваного файлу
    :param timeout: скільки секунд чекати
    :return: True якщо файл існує, інакше False
    """
    for _ in range(timeout):
        if os.path.exists(file_path):
            return True
        time.sleep(1)
    return False

def create_random_file(directory='.', file_extension='.txt', content_length=100):
    # Генеруємо випадкове ім’я файлу
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + file_extension
    filepath = os.path.join(directory, filename)

    # Генеруємо випадковий вміст
    content = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=content_length))

    # Записуємо у файл
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Створено файл: {filepath}")
    return filepath

def generate_random_name(length):
    # Перша літера велика, далі малі, наприклад: "Povika"
    first_letter = random.choice(string.ascii_uppercase)
    other_letters = ''.join(random.choices(string.ascii_lowercase, k=length-1))
    return first_letter + other_letters

def generate_random_email( length=8):
        # Генеруємо випадкове ім’я користувача
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        # Можна використати список доменів для реалізму
        domains = ["example.com", "testmail.com", "mailinator.com"]
        domain = random.choice(domains)
        # Формуємо email
        return f"{username}@{domain}"

import random

def generate_random_numbers(count: int = 10, min_value: int = 0, max_value: int = 100) -> list[int]:
    """
    Генерує список випадкових чисел.

    :param count: кількість чисел
    :param min_value: мінімальне значення
    :param max_value: максимальне значення
    :return: список випадкових чисел
    """
    return [random.randint(min_value, max_value) for _ in range(count)]


def generate_random_mobile(length: int = 10) -> str:
    """
    Генерує випадковий номер мобільного у вигляді рядка з цифр.

    :param length: довжина номера
    :return: рядок з цифрами (номер)
    """
    return ''.join(random.choices("0123456789", k=length))
