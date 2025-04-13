from data import Data, Urls
from pages.constructor_page import ConstructorPage


class TestConstructor:
    def test_constructor_add_ingredient_counter_increased(self, driver_main_page):
        page = ConstructorPage(driver_main_page)

        drag_and_drop = page.drag_and_drop(page.INGREDIENT_1, page.CONSTRUCTOR_BASKET)
        drag_and_drop.perform()

        counter = driver_main_page.find_element(*page.COUNTER)

        assert int(counter.text) == Data.EXPECTED_NUMBER_OF_INGREDIENTS

    def test_constructor_ingredient_details(self, driver_main_page):
        page = ConstructorPage(driver_main_page)

        ingredient = driver_main_page.find_element(*page.INGREDIENT_1)
        ingredient.click()

        page.wait_for_visibility_of_element(page.INGREDIENT_DETAIL)
        ingredient_detail = driver_main_page.find_element(*page.INGREDIENT_DETAIL)

        assert ingredient_detail.text == Data.INGREDIENT_DETAILS

    def test_constructor_ingredient_details_close(self, driver_main_page):
        page = ConstructorPage(driver_main_page)

        ingredient = driver_main_page.find_element(*page.INGREDIENT_1)
        ingredient.click()

        page.wait_for_visibility_of_element(page.INGREDIENT_DETAIL)

        close_button = driver_main_page.find_element(*page.CLOSE_BUTTON)
        close_button.click()

        page.wait_for_invisibility_of_element(page.INGREDIENT_DETAIL)
        ingredient_detail = driver_main_page.find_element(*page.INGREDIENT_DETAIL)

        assert not ingredient_detail.is_displayed()

    def test_constructor_make_order_with_auth_user(self, driver_main_page):
        page = ConstructorPage(driver_main_page)

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

        drag_and_drop = page.drag_and_drop(page.INGREDIENT_1, page.CONSTRUCTOR_BASKET)
        drag_and_drop.perform()

        create_order_button = driver_main_page.find_element(*page.CREATE_ORDER_BUTTON)
        create_order_button.click()

        page.wait_for_visibility_of_element(page.MODAL_WINDOW)

        status = driver_main_page.find_element(*page.ORDER_STATUS)

        assert status.text == Data.ORDER_IN_PROGRESS_STATUS
