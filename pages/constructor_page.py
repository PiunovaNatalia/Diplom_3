from pages.base_page import BasePage
import allure


class ConstructorPage(BasePage):
    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)
