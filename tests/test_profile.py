from data import Data, Urls
from pages.profile_page import ProfilePage
import allure


class TestProfile:
    @allure.title("Тестирование открытия профиля пользователя после аторизации")
    def test_profile_open(self, driver_main_page):
        page = ProfilePage(driver_main_page)
        page.click_login_in_account_button()

        page.set_email(Data.TEST_EMAIL)
        page.set_password(Data.TEST_PASSWORD)
        page.click_login_button()

        page.wait_for_visibility_of_title()
        page.click_profile_button()
        profile_title = page.get_profile_title()

        assert profile_title.is_displayed()

    @allure.title("Тестирование открытия страницы истории заказов в профиле")
    def test_profile_order_history_open(self, driver_main_page):
        page = ProfilePage(driver_main_page)
        page.click_login_in_account_button()

        page.set_email(Data.TEST_EMAIL)
        page.set_password(Data.TEST_PASSWORD)
        page.click_login_button()

        page.wait_for_visibility_of_title()
        page.click_profile_button()

        page.click_order_history_button()

        assert page.get_current_url() == Urls.ORDER_HISTORY_URL
