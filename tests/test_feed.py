from data import Data, Urls
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

    def test_feed_order_exist(self, driver_main_page):
        page = FeedPage(driver_main_page)
        page.login_from_main_page()
        page.make_order()
        created_order_number = page.get_order_number()

        login_button = page.get_element(page.PROFILE_BUTTON)
        login_button.click()
        page.wait_for_visibility_of_element(page.PROFILE_TITLE)
        order_history_button = page.get_element(page.ORDER_HISTORY_BUTTON)
        order_history_button.click()

        page.page_scroll_down()
        page.page_scroll_down()
        page.page_scroll_down()

        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys

        # ORDERS_HISTORY_LIST = (By.XPATH, f".//ul[contains(@class,'OrderHistory_list')]/li/p[contains(text(),'{created_order_number}')]")

        # ORDERS_HISTORY_LIST = (By.XPATH, f".//ul[contains(@class,'OrderHistory_list')]/li/p[contains(text(),'{created_order_number}')]")
        # ORDERS_P = (By.XPATH, ".//ul[contains(@class,'OrderHistory_list')]/p[contains(@class,'text_type_digits-default')]")
        LI = (By.XPATH, ".//ul[contains(@class,'OrderHistory_list')]/li")
        page.wait_for_visibility_of_element(page.ORDERS_HISTORY_LIST)

        el = page.get_element(LI)
        # actions.move_to_element(el)
        # actions.send_keys(Keys.DOWN).perform()

        # ActionChains(driver_main_page).move_to_element(el).send_keys(Keys.DOWN).perform()


        lst = page.get_element(page.ORDERS_HISTORY_LIST)
        for element in lst:
            hover = ActionChains(driver_main_page).move_to_element(element)

            hover.perform()
            print(element)


        # last_order_number = lst[-1].text

        # print(lst, type(lst))




        # assert order_number == 1


        # create_order_button = page.get_element(page.FEED_BUTTON)
        # create_order_button.click()
        # page.wait_for_visibility_of_element(page.ORDER_FEED_TITLE)
        #
        # order_item = page.get_element(page.ORDER_ITEM)
        # order_item.click()
        #
        # page.wait_for_visibility_of_element(page.ORDER_MODAL_WINDOW)
        # order_modal_window = page.get_element(page.ORDER_MODAL_WINDOW)
        #
        # assert order_modal_window.is_displayed()

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