from data import Urls
from pages.feed_page import FeedPage


class TestFeed:
    def test_feed_open_order_details(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()

        create_order_button = page.get_element(page.FEED_BUTTON)
        create_order_button.click()
        page.wait_for_visibility_of_element(page.ORDER_FEED_TITLE)

        order_item = page.get_element(page.ORDER_ITEM)
        order_item.click()

        page.wait_for_visibility_of_element(page.ORDER_MODAL_WINDOW)
        order_modal_window = page.get_element(page.ORDER_MODAL_WINDOW)

        assert order_modal_window.is_displayed()

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

    def test_feed_order_appeared_in_progress(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()

        order_number = page.make_order()
        page.open_feed_page()
        page.wait_for_visibility_of_element(page.ORDERS_IN_PROGRESS)
        orders_in_progress = page.get_element(page.ORDERS_IN_PROGRESS)

        assert order_number == orders_in_progress.text[1:]

    def test_feed_order_exist_on_history_page_and_feed_page(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()
        page.make_order()
        created_order_number = page.get_order_number()

        login_button = page.get_element(page.PROFILE_BUTTON)
        login_button.click()
        page.wait_for_visibility_of_element(page.PROFILE_TITLE)
        order_history_button = page.get_element(page.ORDER_HISTORY_BUTTON)
        order_history_button.click()

        page.wait_for_visibility_of_element(page.ORDER_HISTORY_LIST)

        orders_history_order_numbers = []
        orders_feed_order_numbers = []

        orders_history_list = page.get_elements(page.ORDER_HISTORY_LIST_ITEM)

        for order in orders_history_list:
            orders_history_order_numbers.append(order.text[2:])

        assert created_order_number in orders_history_order_numbers

        page.open_feed_page()
        page.wait_for_visibility_of_element(page.ORDER_FEED_LIST)
        orders_feed_list = page.get_elements(page.ORDER_FEED_LIST_ITEM)

        for order in orders_feed_list:
            orders_feed_order_numbers.append(order.text[2:])

        assert created_order_number in orders_feed_order_numbers
