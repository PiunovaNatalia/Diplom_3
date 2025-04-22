from data import Data, Urls
from pages.forgot_password_page import ForgotPasswordPage
import allure


class TestForgotPassword:
    @allure.title("Тестирование восстановления пароля")
    def test_password_recovery(self, driver_main_page):
        page = ForgotPasswordPage(driver_main_page)
        page.open_page(Urls.LOGIN_URL)
        page.wait_for_visibility_of_element(page.LOGIN_H2)
        page.click_forgot_password_button()
        page.set_email(Data.TEST_EMAIL)
        page.click_password_recovery_button()
        page.set_password(Data.TEST_PASSWORD)
        page.click_hide_password_button()

        active_input = page.get_active_input()
        save_button = page.get_save_button()

        assert active_input.is_displayed() and save_button.is_displayed()
