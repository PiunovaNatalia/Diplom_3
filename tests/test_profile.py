from data import Data, Urls
from pages.profile_page import ProfilePage


class TestProfile:
    def test_profile_open(self, driver_main_page):
        page = ProfilePage(driver_main_page)

        button = driver_main_page.find_element(*page.LOGIN_IN_ACCOUNT_BUTTON)
        button.click()

        page.wait_for_visibility_of_element(page.LOGIN_H2)

        email_input = driver_main_page.find_element(*page.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)

        password_input = driver_main_page.find_element(*page.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)

        login_button = driver_main_page.find_element(*page.LOGIN_BUTTON)
        login_button.click()

        page.wait_for_visibility_of_element(page.CONSTRUCTOR_TITLE)

        login_button = driver_main_page.find_element(*page.PROFILE_BUTTON)
        login_button.click()

        page.wait_for_visibility_of_element(page.PROFILE_TITLE)
        profile_title = driver_main_page.find_element(*page.PROFILE_TITLE)

        assert profile_title.is_displayed()

    def test_profile_order_history_open(self, driver_main_page):
        page = ProfilePage(driver_main_page)

        button = driver_main_page.find_element(*page.LOGIN_IN_ACCOUNT_BUTTON)
        button.click()

        page.wait_for_visibility_of_element(page.LOGIN_H2)

        email_input = driver_main_page.find_element(*page.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)

        password_input = driver_main_page.find_element(*page.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)

        login_button = driver_main_page.find_element(*page.LOGIN_BUTTON)
        login_button.click()

        page.wait_for_visibility_of_element(page.CONSTRUCTOR_TITLE)

        login_button = driver_main_page.find_element(*page.PROFILE_BUTTON)
        login_button.click()

        page.wait_for_visibility_of_element(page.PROFILE_TITLE)
        order_history_button = driver_main_page.find_element(*page.ORDER_HISTORY_BUTTON)
        order_history_button.click()

        url = page.get_current_url()

        assert url == Urls.ORDER_HISTORY_URL