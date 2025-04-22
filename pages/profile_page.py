from pages.base_page import BasePage
import allure
from locators import Locators


class ProfilePage(BasePage):
    PASSWORD_INPUT = Locators.PASSWORD_INPUT
    EMAIL_INPUT = Locators.EMAIL_INPUT
    LOGIN_IN_ACCOUNT_BUTTON = Locators.LOGIN_IN_ACCOUNT_BUTTON
    LOGIN_H2 = Locators.LOGIN_H2
    LOGIN_BUTTON = Locators.LOGIN_BUTTON
    CONSTRUCTOR_TITLE = Locators.CONSTRUCTOR_TITLE
    PROFILE_BUTTON = Locators.PROFILE_BUTTON
    PROFILE_TITLE = Locators.PROFILE_TITLE
    ORDER_HISTORY_BUTTON = Locators.ORDER_HISTORY_BUTTON

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Вводим почтовый адрес')
    def set_email(self, email):
        self.get_element(self.EMAIL_INPUT).send_keys(email)

    @allure.step('Нажимаем на кнопку входа в аккаунт')
    def click_login_in_account_button(self):
        self.get_element(self.LOGIN_IN_ACCOUNT_BUTTON).click()
        self.wait_for_visibility_of_element(self.LOGIN_H2)

    @allure.step('Нажимаем на кнопку авторизации')
    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    @allure.step('Ожидаем отображения заголовка')
    def wait_for_visibility_of_title(self):
        self.wait_for_visibility_of_element(self.CONSTRUCTOR_TITLE)

    @allure.step('Нажимаем на кнопку провиля')
    def click_profile_button(self):
        self.get_element(self.PROFILE_BUTTON).click()
        self.wait_for_visibility_of_element(self.PROFILE_TITLE)

    @allure.step('Открываем историю заказов')
    def click_order_history_button(self):
        self.get_element(self.ORDER_HISTORY_BUTTON).click()

    @allure.step('Получаем заголовок профиля')
    def get_profile_title(self):
        return self.get_element(self.PROFILE_TITLE)
