from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import allure
from data import Data


class BasePage:
    LOGIN_H2 = (By.XPATH, ".//h2[text()='Вход']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # Поле для ввода имейла
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")  # Поле для ввода имейла
    PROFILE_TITLE = (By.XPATH, ".//a[text()='Профиль']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок страницы конструктора
    INGREDIENT_1 = (By.XPATH, "(.//a[contains(@class,'BurgerIngredient')])[1]")
    CONSTRUCTOR_BASKET = (By.XPATH, ".//ul[contains(@class,'BurgerConstructor')]")
    MODAL_WINDOW = (By.XPATH, ".//div[contains(@class,'Modal_modal')]")
    INGREDIENT_DETAIL = (By.XPATH, ".//h2[contains(@class,'Modal_modal__title')]")
    CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class,'Modal_modal__close')]")
    COUNTER = (By.XPATH, ".//div[contains(@class,'counter_counter')]")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  #  Кнопка личный кабинет в шапке сайта
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")
    ORDER_STATUS = (By.XPATH, "(.//div[contains(@class,'Modal_modal__textContainer')]/p)[1]")
    MODAL_TITLE = (By.XPATH, ".//h2[contains(@class,'Modal_modal__title')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ожидаем отображения элемента на странице')
    def wait_for_visibility_of_element(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(xpath))

    # def text_to_be_present_in_element(self, xpath, text):
    #     WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(xpath, text))

    @allure.step('Ожидаем скрытия элемента на странице')
    def wait_for_invisibility_of_element(self, xpath):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(xpath))

    @allure.step('Получаем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Прокручиваем страницу вниз')
    def page_scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Ожидаем открытия окна')
    def wait_for_number_of_windows_to_be_two(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

    @allure.step('Ищем элемент на странице')
    def get_element(self, xpath):
        return self.driver.find_element(*xpath)

    @allure.step('Ищем элементы на странице')
    def get_elements(self, xpath):
        return self.driver.find_elements(*xpath)

    @allure.step('Кликаем по кнопке')
    def click(self, xpath):
        self.get_element(xpath).click()

    @allure.step('Переключаемся на окно №{window_number}')
    def switch_to_window_by_num(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Получаем количество открытых окон')
    def get_number_of_open_windows(self):
        return len(self.driver.window_handles)

    @allure.step('Выполняем скрипт по нажатию кнопки')
    def execute_click_script(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получаем элемент')
    def get_wait_element(self, xpath):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(xpath))

    @allure.step('Авторизация пользователя')
    def login_from_main_page(self):
        button = self.get_element(self.LOGIN_IN_ACCOUNT_BUTTON)
        button.click()
        self.wait_for_visibility_of_element(self.LOGIN_H2)
        email_input = self.get_element(self.EMAIL_INPUT)
        email_input.send_keys(Data.TEST_EMAIL)
        password_input = self.get_element(self.PASSWORD_INPUT)
        password_input.send_keys(Data.TEST_PASSWORD)
        login_button = self.get_element(self.LOGIN_BUTTON)
        login_button.click()
        self.wait_for_visibility_of_element(self.CONSTRUCTOR_TITLE)

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_and_drop(self, drag, drop):
        drag = self.get_wait_element(drag)
        drop = self.get_wait_element(drop)

        return ActionChains(self.driver).drag_and_drop(drag, drop)

    # @allure.step('Прокручиваем страницу вниз')
    # def page_scroll_down(self):
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")