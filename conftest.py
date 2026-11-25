import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--language", default="en", help="Storefront browser language")
    parser.addoption("--headed", action="store_true", help="Show the Chrome window")


@pytest.fixture
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": request.config.getoption("--language")}
    )
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument('--window-size=1440,1000')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(25)
    try:
        yield driver
    finally:
        driver.quit()
