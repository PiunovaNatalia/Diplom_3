from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    ORDER_ITEM = (By.XPATH, "(.//li[contains(@class,'OrderHistory_listItem')])[1]")
    ORDER_FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")
    ORDER_MODAL_WINDOW = (By.XPATH, ".//div[contains(@class,'Modal_orderBox')]")
    DETAILS = (By.XPATH, ".//p[text()='Cостав']")
    # MODAL_OVERLAY = (By.XPATH, ".//div[contains(@class,'Modal_modal_overlay')]")
    MODAL_OPENED = (By.XPATH, ".//div[contains(@class,'Modal_modal_opened')]")
    # ORDERS_P = (By.XPATH, ".//p[contains(@class,'text_type_digits-default')]")  # li[contains(@class,'OrderHistory_listItem')]/
    ORDERS_P = (By.XPATH, ".//div[contains(@class,'OrderHistory_textBox')]/p[contains(@class,'text_type_digits-default')]")
    ORDERS_HISTORY = (By.XPATH, ".//div[contains(@class,'OrderHistory_orderHistory')]")

    ORDERS_HISTORY_LIST = (By.XPATH, ".//ul[contains(@class,'OrderHistory_list')]/li")


    COMPLETED_ALL_TIME = (By.XPATH, "(.//p[contains(@class,'OrderFeed_number')])[1]")
    COMPLETED_TODAY = (By.XPATH, "(.//p[contains(@class,'OrderFeed_number')])[2]")


    def make_order(self):
        drag_and_drop = self.drag_and_drop(self.INGREDIENT_1, self.CONSTRUCTOR_BASKET)
        drag_and_drop.perform()

        create_order_button = self.get_element(self.CREATE_ORDER_BUTTON)
        create_order_button.click()

        self.wait_for_visibility_of_element(self.MODAL_WINDOW)

        # status = self.get_element(self.ORDER_STATUS)
        self.wait_for_invisibility_of_element(self.MODAL_OPENED)

        self.wait_for_visibility_of_element(self.CLOSE_BUTTON)

        close_button = self.get_element(self.CLOSE_BUTTON)
        close_button.click()

        # self.wait_for_invisibility_of_element(self.MODAL_OPENED)

    def get_order_number(self):
        return self.get_element(self.MODAL_TITLE).text

    def get_all_time_orders_number(self):
        return self.get_element(self.COMPLETED_ALL_TIME).text

    def get_today_orders_number(self):
        return self.get_element(self.COMPLETED_TODAY).text

    def open_feed_page(self):
        create_order_button = self.get_element(self.FEED_BUTTON)
        create_order_button.click()
        self.wait_for_visibility_of_element(self.ORDER_FEED_TITLE)
