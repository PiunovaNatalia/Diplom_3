from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from data import Data


class ProfilePage(BasePage):
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Кнопка Профиль
    FORGOT_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
    PASSWORD_RECOVERY_H2 = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    HIDE_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class ,'input__icon')]")
    INPUT_STATUS_ACTIVE = (By.XPATH, ".//div[contains(@class ,'input_status_active')]")
    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def set_email(self, email):
        self.get_element(self.EMAIL_INPUT).send_keys(email)

    def click_login_in_account_button(self):
        self.get_element(self.LOGIN_IN_ACCOUNT_BUTTON).click()
        self.wait_for_visibility_of_element(self.LOGIN_H2)

    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    def wait_for_visibility_of_title(self):
        self.wait_for_visibility_of_element(self.CONSTRUCTOR_TITLE)

    def click_profile_button(self):
        self.get_element(self.PROFILE_BUTTON).click()
        self.wait_for_visibility_of_element(self.PROFILE_TITLE)

    def click_order_history_button(self):
        self.get_element(self.ORDER_HISTORY_BUTTON).click()

    def get_profile_title(self):
        return self.get_element(self.PROFILE_TITLE)