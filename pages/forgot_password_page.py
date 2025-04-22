from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ForgotPasswordPage(BasePage):
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  #  Кнопка личный кабинет в шапке сайта
    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Кнопка Профиль
    FORGOT_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
    PASSWORD_RECOVERY_H2 = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    LOGIN_H2 = (By.XPATH, ".//h2[text()='Вход']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")  # Поле ввода пароля
    HIDE_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class ,'input__icon')]")
    INPUT_STATUS_ACTIVE = (By.XPATH, ".//div[contains(@class ,'input_status_active')]")

    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")

    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # Поле для ввода имейла

    @allure.step('Вводим адрес')
    def set_email(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def click_forgot_password_button(self):
        self.click(self.FORGOT_PASSWORD_BUTTON)
        self.wait_for_visibility_of_element(self.PASSWORD_RECOVERY_H2)

    def click_password_recovery_button(self):
        self.click(self.RECOVERY_BUTTON)
        self.wait_for_visibility_of_element(self.PASSWORD_INPUT)

    def click_hide_password_button(self):
        self.click(self.HIDE_PASSWORD_BUTTON)

    def get_active_input(self):
        return self.get_element(self.INPUT_STATUS_ACTIVE)

    def get_save_button(self):
        return self.get_element(self.SAVE_BUTTON)

    def wait_for_visibility_of_login_title(self):
        self.wait_for_visibility_of_element(self.LOGIN_H2)