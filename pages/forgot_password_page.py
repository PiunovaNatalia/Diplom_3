from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators import Locators
import allure


class ForgotPasswordPage(BasePage):
    PERSONAL_ACCOUNT_BUTTON = Locators.PERSONAL_ACCOUNT_BUTTON
    PROFILE_LINK = Locators.PROFILE_LINK
    FORGOT_PASSWORD_BUTTON = Locators.FORGOT_PASSWORD_BUTTON
    PASSWORD_RECOVERY_H2 = Locators.PASSWORD_RECOVERY_H2
    LOGIN_H2 = Locators.LOGIN_H2
    PASSWORD_INPUT = Locators.PASSWORD_INPUT
    HIDE_PASSWORD_BUTTON = Locators.HIDE_PASSWORD_BUTTON
    INPUT_STATUS_ACTIVE = Locators.INPUT_STATUS_ACTIVE
    RECOVERY_BUTTON = Locators.RECOVERY_BUTTON
    SAVE_BUTTON = Locators.SAVE_BUTTON
    EMAIL_INPUT = Locators.EMAIL_INPUT

    @allure.step('Вводим адрес')
    def set_email(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Нажимаем на кнопку восстановления пароля')
    def click_forgot_password_button(self):
        self.click(self.FORGOT_PASSWORD_BUTTON)
        self.wait_for_visibility_of_element(self.PASSWORD_RECOVERY_H2)

    @allure.step('Нажимаем на кнопку восстановить пароль')
    def click_password_recovery_button(self):
        self.click(self.RECOVERY_BUTTON)
        self.wait_for_visibility_of_element(self.PASSWORD_INPUT)

    @allure.step('Скрываем или показываем введенный пароль')
    def click_hide_password_button(self):
        self.click(self.HIDE_PASSWORD_BUTTON)

    @allure.step('Получаем активный элемент ввода')
    def get_active_input(self):
        return self.get_element(self.INPUT_STATUS_ACTIVE)

    @allure.step('Получаем кнопку сохранения')
    def get_save_button(self):
        return self.get_element(self.SAVE_BUTTON)

    @allure.step('Ожидаем отображения заголовка окна логина')
    def wait_for_visibility_of_login_title(self):
        self.wait_for_visibility_of_element(self.LOGIN_H2)