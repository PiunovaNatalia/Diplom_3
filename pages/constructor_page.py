from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure


class ConstructorPage(BasePage):
    COUNTER = (By.XPATH, ".//div[contains(@class,'counter_counter')]")
    MODAL_WINDOW = (By.XPATH, ".//div[contains(@class,'Modal_modal')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_STATUS = (By.XPATH, "(.//div[contains(@class,'Modal_modal__textContainer')]/p)[1]")


    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)
