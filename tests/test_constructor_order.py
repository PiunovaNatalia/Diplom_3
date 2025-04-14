from data import Data
from pages.constructor_page import ConstructorPage


class TestConstructor:
    def test_constructor_add_ingredient_counter_increased(self, driver_main_page):
        page = ConstructorPage(driver_main_page)
        page.drag_and_drop(page.INGREDIENT_1, page.CONSTRUCTOR_BASKET).perform()
        counter = page.get_element(page.COUNTER)

        assert int(counter.text) == Data.EXPECTED_NUMBER_OF_INGREDIENTS

    def test_constructor_ingredient_details(self, driver_main_page):
        page = ConstructorPage(driver_main_page)

        ingredient = page.get_element(page.INGREDIENT_1)
        ingredient.click()

        page.wait_for_visibility_of_element(page.INGREDIENT_DETAIL)
        ingredient_detail = page.get_element(page.INGREDIENT_DETAIL)

        assert ingredient_detail.text == Data.INGREDIENT_DETAILS

    def test_constructor_ingredient_details_close(self, driver_main_page):
        page = ConstructorPage(driver_main_page)

        ingredient = page.get_element(page.INGREDIENT_1)
        ingredient.click()

        page.wait_for_visibility_of_element(page.INGREDIENT_DETAIL)

        close_button = page.get_element(page.CLOSE_BUTTON)
        close_button.click()

        page.wait_for_invisibility_of_element(page.INGREDIENT_DETAIL)
        ingredient_detail = page.get_element(page.INGREDIENT_DETAIL)

        assert not ingredient_detail.is_displayed()

    def test_constructor_make_order_with_auth_user(self, driver_main_page):
        page = ConstructorPage(driver_main_page)
        page.login_from_main_page()

        drag_and_drop = page.drag_and_drop(page.INGREDIENT_1, page.CONSTRUCTOR_BASKET)
        drag_and_drop.perform()

        create_order_button = page.get_element(page.CREATE_ORDER_BUTTON)
        create_order_button.click()

        page.wait_for_visibility_of_element(page.MODAL_WINDOW)

        status = page.get_element(page.ORDER_STATUS)

        assert status.text == Data.ORDER_IN_PROGRESS_STATUS
