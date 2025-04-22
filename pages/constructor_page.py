from pages.base_page import BasePage
import allure


class ConstructorPage(BasePage):
    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    def get_ingredient_counter(self):
        return self.get_element(self.COUNTER)

    def drag_ingredient_to_basket(self):
        self.drag_and_drop(self.INGREDIENT_1, self.CONSTRUCTOR_BASKET).perform()

    def open_ingredient_details_window(self):
        self.get_element(self.INGREDIENT_1).click()
        self.wait_for_visibility_of_element(self.INGREDIENT_DETAIL)


    def close_details_window(self):
        self.get_element(self.CLOSE_BUTTON).click()
        self.wait_for_invisibility_of_element(self.INGREDIENT_DETAIL)

    def get_ingredient_details(self):
        return self.get_element(self.INGREDIENT_DETAIL)

    def create_order_and_get_order_status(self):
        self.get_element(self.CREATE_ORDER_BUTTON).click()
        self.wait_for_visibility_of_element(self.MODAL_WINDOW)

        return self.get_element(self.ORDER_STATUS)
