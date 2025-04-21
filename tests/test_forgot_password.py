from data import Data, Urls
from pages.forgot_password_page import ForgotPasswordPage
import allure


class TestForgotPassword:
    @allure.title("Тестирование восстановления пароля")
    def test_password_recovery(self, driver_main_page):
        page = ForgotPasswordPage(driver_main_page)
        page.open_page(Urls.LOGIN_URL)

        page.wait_for_visibility_of_element(page.LOGIN_H2)

        button = page.get_element(page.FORGOT_PASSWORD_BUTTON)
        button.click()

        page.wait_for_visibility_of_element(page.PASSWORD_RECOVERY_H2)

        page.get_element(page.EMAIL_INPUT)
        page.set_address(Data.TEST_EMAIL)

        button = page.get_element(page.RECOVERY_BUTTON)
        button.click()

        page.wait_for_visibility_of_element(page.PASSWORD_INPUT)

        page.get_element(page.PASSWORD_INPUT)
        page.set_password(Data.TEST_PASSWORD)

        button = page.get_element(page.HIDE_PASSWORD_BUTTON)
        button.click()

        active_input = page.get_element(page.INPUT_STATUS_ACTIVE)
        save_button = page.get_element(page.SAVE_BUTTON)

        assert active_input.is_displayed() and save_button.is_displayed()
