from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
import allure


class ConstructorPage(BasePage):
    INGREDIENT_1 = (By.XPATH, "(.//a[contains(@class,'BurgerIngredient')])[1]")
    CONSTRUCTOR_BASKET = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor')]")
    COUNTER = (By.XPATH, ".//div[contains(@class,'counter_counter')]")
    MODAL_WINDOW = (By.XPATH, ".//div[contains(@class,'Modal_modal')]")
    INGREDIENT_DETAIL = (By.XPATH, ".//h2[contains(@class,'Modal_modal__title')]")
    CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class,'Modal_modal__close')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_STATUS = (By.XPATH, "(.//div[contains(@class,'Modal_modal__textContainer')]/p)[1]")


    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)

    @allure.step('')
    def get_wait_element(self, xpath):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(xpath))

    @allure.step('')
    def drag_and_drop(self, drag, drop):
        drag = self.get_wait_element(drag)
        drop = self.get_wait_element(drop)

        return ActionChains(self.driver).drag_and_drop(drag, drop)


