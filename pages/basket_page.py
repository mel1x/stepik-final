from .base_page import BasePage
from .locators import BasketPageLocators as Locators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(Locators.ITEMS), "Basket contains items"
        assert "Your basket is empty" in self.find(Locators.SUMMARY).text, "Empty basket message is missing"
