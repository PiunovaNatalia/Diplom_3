from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем отображения элемента на странице')
    def wait_for_visibility_of_element(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath))

    @allure.step('Ожидаем скрытия элемента на странице')
    def wait_for_invisibility_of_element(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(xpath))

    @allure.step('Получаем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ищем элемент на странице')
    def get_element(self, xpath):
        return self.driver.find_element(*xpath)

    @allure.step('Ищем элементы на странице')
    def get_elements(self, xpath):
        return self.driver.find_elements(*xpath)

    @allure.step('Кликаем по кнопке')
    def click(self, xpath):
        self.get_element(xpath).click()

    @allure.step('Получаем элемент')
    def get_wait_element(self, xpath):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(xpath))

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_and_drop(self, drag, drop):
        drag = self.get_wait_element(drag)
        drop = self.get_wait_element(drop)
        return ActionChains(self.driver).drag_and_drop(drag, drop).pause(5)
