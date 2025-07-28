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
