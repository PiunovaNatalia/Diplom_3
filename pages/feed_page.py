from pages.base_page import BasePage
import allure
from data import Data
from locators import Locators


class FeedPage(BasePage):
    FEED_BUTTON = Locators.FEED_BUTTON
    ORDER_ITEM = Locators.ORDER_ITEM
    ORDER_FEED_TITLE = Locators.ORDER_FEED_TITLE
    ORDER_MODAL_WINDOW = Locators.ORDER_MODAL_WINDOW
    MODAL_OPENED = Locators.MODAL_OPENED
    ORDER_HISTORY_LIST = Locators.ORDER_HISTORY_LIST
    ORDER_HISTORY_LIST_ITEM = Locators.ORDER_HISTORY_LIST_ITEM
    ORDER_FEED_LIST = Locators.ORDER_FEED_LIST
    ORDER_FEED_LIST_ITEM = Locators.ORDER_FEED_LIST_ITEM
    COMPLETED_ALL_TIME = Locators.COMPLETED_ALL_TIME
    COMPLETED_TODAY = Locators.COMPLETED_TODAY
    ORDER_NUMBER = Locators.ORDER_NUMBER
    ORDERS_IN_PROGRESS = Locators.ORDERS_IN_PROGRESS
    INGREDIENT_1 = Locators.INGREDIENT_1
    CONSTRUCTOR_BASKET = Locators.CONSTRUCTOR_BASKET
    MODAL_WINDOW = Locators.MODAL_WINDOW
    CLOSE_BUTTON = Locators.CLOSE_BUTTON
    CREATE_ORDER_BUTTON = Locators.CREATE_ORDER_BUTTON
    MODAL_TITLE = Locators.MODAL_TITLE
    LOGIN_IN_ACCOUNT_BUTTON = Locators.LOGIN_IN_ACCOUNT_BUTTON
    PROFILE_BUTTON = Locators.PROFILE_BUTTON
    PROFILE_TITLE = Locators.PROFILE_TITLE
    ORDER_HISTORY_BUTTON = Locators.ORDER_HISTORY_BUTTON
    LOGIN_H2 = Locators.LOGIN_H2
    PASSWORD_INPUT = Locators.PASSWORD_INPUT
    EMAIL_INPUT = Locators.EMAIL_INPUT
    LOGIN_BUTTON = Locators.LOGIN_BUTTON
    CONSTRUCTOR_TITLE = Locators.CONSTRUCTOR_TITLE


    @allure.step("Совершение заказа")
    def make_order(self):
        drag_and_drop = self.drag_and_drop(self.INGREDIENT_1, self.CONSTRUCTOR_BASKET)
        drag_and_drop.perform()

        create_order_button = self.get_element(self.CREATE_ORDER_BUTTON)
        create_order_button.click()

        self.wait_for_visibility_of_element(self.MODAL_WINDOW)
        self.wait_for_invisibility_of_element(self.MODAL_OPENED)

        order_number = self.get_element(self.ORDER_NUMBER).text

        self.wait_for_visibility_of_element(self.CLOSE_BUTTON)
        close_button = self.get_element(self.CLOSE_BUTTON)
        close_button.click()

        return order_number

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        return self.get_element(self.MODAL_TITLE).text

    @allure.step("Получение количества заказов за все время")
    def get_all_time_orders_number(self):
        return self.get_element(self.COMPLETED_ALL_TIME).text

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_number(self):
        return self.get_element(self.COMPLETED_TODAY).text

    @allure.step("Открытие ленты заказов")
    def open_feed_page(self):
        create_order_button = self.get_element(self.FEED_BUTTON)
        create_order_button.click()
        self.wait_for_visibility_of_element(self.ORDER_FEED_TITLE)

    @allure.step('Открываем ленту заказов')
    def click_order_feed_button(self):
        self.click(self.FEED_BUTTON)

    @allure.step('Ожидаем открытия ленты заказов')
    def wait_for_visibility_of_order_feed_title(self):
        self.wait_for_visibility_of_element(self.ORDER_FEED_TITLE)

    @allure.step('Нажимаем на элемент заказа')
    def click_order_item_button(self):
        self.click(self.ORDER_ITEM)
        self.wait_for_visibility_of_element(self.ORDER_MODAL_WINDOW)

    @allure.step('Получаем подробную информацию об элементе')
    def get_order_item_details(self):
        return self.get_element(self.ORDER_MODAL_WINDOW)

    @allure.step('Ожидаем появления закзаов в работе')
    def wait_for_visibility_of_orders_in_progress(self):
        self.wait_for_visibility_of_element(self.ORDERS_IN_PROGRESS)

    @allure.step('Получаем заказы в работе')
    def get_order_in_progress(self):
        return self.get_element(self.ORDERS_IN_PROGRESS)

    @allure.step('Нажимамем на кнопку открытия профиля')
    def click_profile_button(self):
        self.click(self.PROFILE_BUTTON)
        self.wait_for_visibility_of_element(self.PROFILE_TITLE)

    @allure.step('Нажимаем на кнопку открытия истории заказов')
    def click_order_history_button(self):
        self.click(self.ORDER_HISTORY_BUTTON)
        self.wait_for_visibility_of_element(self.ORDER_HISTORY_LIST)

    @allure.step('Получаем историю заказов')
    def get_orders_history_list(self):
        return self.get_elements(self.ORDER_HISTORY_LIST_ITEM)

    @allure.step('Получаем список заказов')
    def get_orders_feed_list(self):
        self.wait_for_visibility_of_element(self.ORDER_FEED_LIST)
        return self.get_elements(self.ORDER_FEED_LIST_ITEM)

    @allure.step('Нажимаем кнопку входа в аккаунт')
    def click_login_in_account_button(self):
        self.get_element(self.LOGIN_IN_ACCOUNT_BUTTON).click()
        self.wait_for_visibility_of_element(self.LOGIN_H2)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('Вводим почтовый адрес')
    def set_email(self, email):
        self.get_element(self.EMAIL_INPUT).send_keys(email)

    @allure.step('Нажимаем кнопку авторизации')
    def click_login_button(self):
        self.get_element(self.LOGIN_BUTTON).click()

    @allure.step('Авторизация пользователя')
    def login_from_main_page(self):
        self.click_login_in_account_button()
        self.set_email(Data.TEST_EMAIL)
        self.set_password(Data.TEST_PASSWORD)
        self.click_login_button()
        self.wait_for_visibility_of_element(self.CONSTRUCTOR_TITLE)
