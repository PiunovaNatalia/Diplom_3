from pages.base_page import BasePage
import allure
from data import Data
from locators import Locators


class ConstructorPage(BasePage):
    PASSWORD_INPUT = Locators.PASSWORD_INPUT
    COUNTER = Locators.COUNTER
    INGREDIENT_1 = Locators.INGREDIENT_1
    CONSTRUCTOR_BASKET = Locators.CONSTRUCTOR_BASKET
    INGREDIENT_DETAIL = Locators.INGREDIENT_DETAIL
    CLOSE_BUTTON = Locators.CLOSE_BUTTON
    CREATE_ORDER_BUTTON = Locators.CREATE_ORDER_BUTTON
    MODAL_WINDOW = Locators.MODAL_WINDOW
    ORDER_STATUS = Locators.ORDER_STATUS
    LOGIN_IN_ACCOUNT_BUTTON = Locators.LOGIN_IN_ACCOUNT_BUTTON
    LOGIN_H2 = Locators.LOGIN_H2
    EMAIL_INPUT = Locators.EMAIL_INPUT
    LOGIN_BUTTON = Locators.LOGIN_BUTTON
    CONSTRUCTOR_TITLE = Locators.CONSTRUCTOR_TITLE

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Получаем счетчик ингредиента')
    def get_ingredient_counter(self):
        return self.get_element(self.COUNTER)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_ingredient_to_basket(self):
        self.drag_and_drop(self.INGREDIENT_1, self.CONSTRUCTOR_BASKET).perform()

    @allure.step('Открываем окно с информацией об ингредиенте')
    def open_ingredient_details_window(self):
        self.get_element(self.INGREDIENT_1).click()
        self.wait_for_visibility_of_element(self.INGREDIENT_DETAIL)

    @allure.step('Закрываем окно с информацией')
    def close_details_window(self):
        self.get_element(self.CLOSE_BUTTON).click()
        self.wait_for_invisibility_of_element(self.INGREDIENT_DETAIL)

    @allure.step('Получаем информацию об ингредиенте')
    def get_ingredient_details(self):
        return self.get_element(self.INGREDIENT_DETAIL)

    @allure.step('Создаем заказ и получаем его статус')
    def create_order_and_get_order_status(self):
        self.get_element(self.CREATE_ORDER_BUTTON).click()
        self.wait_for_visibility_of_element(self.MODAL_WINDOW)
        return self.get_element(self.ORDER_STATUS)

    @allure.step('Нажимаем на кнопку входа в аккаунт')
    def click_login_in_account_button(self):
        self.get_element(self.LOGIN_IN_ACCOUNT_BUTTON).click()
        self.wait_for_visibility_of_element(self.LOGIN_H2)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Вводим почтовый адрес')
    def set_email(self, email):
        self.get_element(self.EMAIL_INPUT).send_keys(email)

    @allure.step('Нажимаем на кнопку авторизации')
    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    @allure.step('Авторизация пользователя')
    def login_from_main_page(self):
        self.click_login_in_account_button()
        self.set_email(Data.TEST_EMAIL)
        self.set_password(Data.TEST_PASSWORD)
        self.click_login_button()
        self.wait_for_visibility_of_element(self.CONSTRUCTOR_TITLE)
