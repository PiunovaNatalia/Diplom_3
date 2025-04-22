import pytest
from data import Urls
from helpers import WebdriverFactory


@pytest.fixture(scope="function", params=["Chrome"])
def driver(request):
    """Главный Webdriver."""

    driver = WebdriverFactory.get_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver_main_page(driver):
    """Дополнительный Webdriver с открытием главной страницы."""

    driver.get(Urls.MAIN_PAGE_URL)
    return driver
