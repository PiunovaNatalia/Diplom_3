from selenium.webdriver.common.by import By


class Locators:
    """Локаторы для поиска элементов на страницах сайта."""

    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")  # Поле ввода имейла
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопки входа на сайт на странице входа
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка регистрации на сайте
    SECTION_TITLE = (By.CSS_SELECTOR, ".text_type_main-large")  # Заголовка на странице конструктора (Соберите бургер)
    REGISTER_NAME_INPUT = (By.XPATH, "(.//input[@name='name'])[1]") # Поле для ввода имени на странице регистрации
    REGISTER_EMAIL_INPUT = (By.XPATH, "(.//input[@name='name'])[2]")  # Поле для ввода имейла на странице регистрации
    LOGIN_PAGE_TITLE = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок на странице входа
    INCORRECT_PASSWORD_WARNING = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Предупреждение о неправильно введенном пароле
    LOGIN_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка Войти в аккаунт
    LOGIN_THROUGH_REGISTER_PAGE_LINK = (By.XPATH, ".//a[text()='Войти']")  # Кнопка войти на странице после регистрации

    LOGOTYPE = (By.XPATH, ".//a[@href='/']")  # Ссылка-логотип
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка для выход из личного кабинета
    BREAD_TAB_BUTTON = (By.XPATH, "(.//div[contains(@class,'tab_tab')]/span[text()='Булки'])")  # Таб-кнопка для раздела с булками
    SAUCES_TAB_BUTTON = (By.XPATH, "(.//div[contains(@class,'tab_tab')]/span[text()='Соусы'])")  # Таб-кнопка для раздела с соусами
    FILLING_TAB_BUTTON = (By.XPATH, "(.//div[contains(@class,'tab_tab')]/span[text()='Начинки'])")  # Таб-кнопка для раздела с начинками
    SELECTED_BREAD_TAB = (By.XPATH, "(.//div[contains(@class,'tab_type_current')]/span[text()='Булки'])")  # Таб-кнопка НАЖАТАЯ для раздела с булками
    SELECTED_SAUCES_TAB = (By.XPATH, "(.//div[contains(@class,'tab_type_current')]/span[text()='Соусы'])")  # Таб-кнопка НАЖАТАЯ для раздела с соусами
    SELECTED_FILLING_TAB = (By.XPATH, "(.//div[contains(@class,'tab_type_current')]/span[text()='Начинки'])")  # Таб-кнопка НАЖАТАЯ для раздела с начинками