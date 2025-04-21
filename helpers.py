import random
import uuid

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service


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

    @staticmethod
    def make_list_of_order_numbers(source_data):
        order_numbers = []
        for order in source_data:
            order_numbers.append(order.text[2:])
        return order_numbers


class WebdriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "Chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            return driver
        elif browser_name == "Firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            return driver

