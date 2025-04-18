from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service

import pytest
from data import Urls


class WebdriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "Chrome":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            return driver
        elif browser_name == "Firefox":
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            return driver


@pytest.fixture(scope="function", params=["Chrome"])
def driver(request):
    driver = WebdriverFactory.get_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_main_page(driver):
    driver.get(Urls.MAIN_PAGE_URL)

    yield driver
