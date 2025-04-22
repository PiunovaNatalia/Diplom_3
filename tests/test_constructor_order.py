from data import Data
from pages.constructor_page import ConstructorPage
import allure


class TestConstructor:
    @allure.title("Счетчик ингредиентов увеличивается после добавления ингредиента в заказ")
    def test_constructor_add_ingredient_counter_increased(self, driver_main_page):
        page = ConstructorPage(driver_main_page)
        page.drag_ingredient_to_basket()
        counter = page.get_ingredient_counter().text

        assert int(counter) == Data.EXPECTED_NUMBER_OF_INGREDIENTS

    @allure.title("Тестирование отображения окна с информацией об ингредиенте")
    def test_constructor_ingredient_details(self, driver_main_page):
        page = ConstructorPage(driver_main_page)
        page.open_ingredient_details_window()
        ingredient_details_text = page.get_ingredient_details().text

        assert ingredient_details_text == Data.INGREDIENT_DETAILS

    @allure.title("Тестирование закрытия окна с информацией об ингредиенте")
    def test_constructor_ingredient_details_close(self, driver_main_page):
        page = ConstructorPage(driver_main_page)
        page.open_ingredient_details_window()
        page.close_details_window()
        ingredient_details = page.get_ingredient_details()

        assert not ingredient_details.is_displayed()

    @allure.title("Тестирование создания заказа с авторизированным пользователем")
    def test_constructor_make_order_with_auth_user(self, driver_main_page):
        page = ConstructorPage(driver_main_page)
        page.login_from_main_page()
        page.drag_ingredient_to_basket()
        status = page.create_order_and_get_order_status().text

        assert status == Data.ORDER_IN_PROGRESS_STATUS
