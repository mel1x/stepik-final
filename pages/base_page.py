from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def find(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        self.find(BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert not self.is_not_element_present(BasePageLocators.LOGIN_LINK), "Login link is missing"

    def go_to_basket(self):
        self.find(BasePageLocators.BASKET_LINK).click()

    def should_be_authorized_user(self):
        assert not self.is_not_element_present(BasePageLocators.USER_ICON), "User is not signed in"
