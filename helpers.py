import random
import uuid


class Helper:
    """Функции для генерации случайных паролей и имейлов."""

    @staticmethod
    def generate_email():
        """Функция для генерации имейлов"""

        return f"piunova_natalia_{random.randint(1, 1000)}@yandex.ru"

    @staticmethod
    def generate_password():

        """Функция для генерации паролей"""
        return f"{uuid.uuid4()}"