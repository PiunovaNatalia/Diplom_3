from data import Urls
from pages.feed_page import FeedPage
from helpers import Helper
import allure


class TestFeed:
    @allure.title("Тестирование открытия окна с дополнительной информацией о заказе")
    def test_feed_open_order_details(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()

        page.click_order_feed_button()
        page.wait_for_visibility_of_order_feed_title()

        page.click_order_item_button()
        item_details_modal = page.get_order_item_details()

        assert item_details_modal.is_displayed()

    @allure.title("Тестирование увеличения общего числа заказов после совершения заказа")
    def test_feed_order_all_amount_increased(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()
        page.open_feed_page()

        all_time_before_order = page.get_all_time_orders_number()

        page.open_page(Urls.MAIN_PAGE_URL)
        page.make_order()
        page.open_feed_page()
        all_time_after_order = page.get_all_time_orders_number()

        assert all_time_before_order < all_time_after_order

    @allure.title("Тестирование увеличения числа заказов за сегодня после совершения заказа")
    def test_feed_order_today_amount_increased(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()
        page.open_feed_page()

        today_before_order = page.get_today_orders_number()

        page.open_page(Urls.MAIN_PAGE_URL)
        page.make_order()
        page.open_feed_page()
        today_after_order = page.get_today_orders_number()

        assert today_before_order < today_after_order

    @allure.title("Тестирование появления заказа в разделе 'В работе' после совершения заказа")
    def test_feed_order_appeared_in_progress(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()

        order_number = page.make_order()
        page.open_feed_page()
        page.wait_for_visibility_of_orders_in_progress()
        orders_in_progress = page.get_order_in_progress()

        assert order_number == orders_in_progress.text[1:]

    @allure.title("Тестирование отображения нового заказа в истории заказов и в ленте заказов")
    def test_feed_order_exist_on_history_page_and_feed_page(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()
        page.make_order()
        created_order_number = page.get_order_number()
        page.click_profile_button()
        page.click_order_history_button()
        orders_history_list = page.get_orders_history_list()
        orders_history_order_numbers = Helper.make_list_of_order_numbers(orders_history_list)

        assert created_order_number in orders_history_order_numbers

        page.open_feed_page()
        orders_feed_list = page.get_orders_feed_list()
        orders_feed_order_numbers = Helper.make_list_of_order_numbers(orders_feed_list)

        assert created_order_number in orders_feed_order_numbers
