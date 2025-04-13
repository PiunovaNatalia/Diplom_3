from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ProfilePage(BasePage):
    PROFILE_BUTTON = (By.XPATH, ".//p[text()='Личный Кабинет']")  #  Кнопка личный кабинет в шапке сайта



    PROFILE_LINK = (By.XPATH, ".//a[text()='Профиль']")  # Кнопка Профиль
    FORGOT_PASSWORD_BUTTON = (By.XPATH, ".//a[text()='Восстановить пароль']")
    PASSWORD_RECOVERY_H2 = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")
    HIDE_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class ,'input__icon')]")
    INPUT_STATUS_ACTIVE = (By.XPATH, ".//div[contains(@class ,'input_status_active')]")

    RECOVERY_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")

    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[text()='История заказов']")



    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.get_element(self.EMAIL_INPUT).send_keys(address)

    @allure.step('Вводим пароль')
    def set_password(self, password):
        self.get_element(self.PASSWORD_INPUT).send_keys(password)




