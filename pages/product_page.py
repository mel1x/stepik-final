import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.find(Locators.ADD_TO_BASKET).click()

    def solve_promo_quiz(self):
        wait = WebDriverWait(self.browser, 5)
        prompt = wait.until(EC.alert_is_present())
        number = float(prompt.text.split()[2])
        answer = math.log(abs(12 * math.sin(number)))
        prompt.send_keys(str(answer))
        prompt.accept()
        try:
            result = wait.until(EC.alert_is_present())
        except TimeoutException:
            return
        code = result.text
        result.accept()
        print(code)

    def product_title(self):
        return self.find(Locators.TITLE).text

    def product_price(self):
        return self.find(Locators.PRICE).text

    def should_show_added_product(self, expected_title):
        actual_title = self.find(Locators.SUCCESS_TITLE).text
        assert actual_title == expected_title, f"Expected {expected_title!r}, found {actual_title!r}"

    def should_show_correct_basket_total(self, price):
        total = self.find(Locators.BASKET_TOTAL).text
        assert total == price, f"Expected basket total {price!r}, found {total!r}"

    def should_not_show_success_message(self):
        assert self.is_not_element_present(Locators.SUCCESS_TITLE), "Success message is shown"

    def should_hide_success_message(self):
        assert self.is_disappeared(Locators.SUCCESS_TITLE), "Success message did not disappear"
