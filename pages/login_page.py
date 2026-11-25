from .base_page import BasePage
from .locators import LoginPageLocators as Locators


class LoginPage(BasePage):
    def should_be_login_page(self):
        assert "login" in self.browser.current_url, "Login URL is missing"
        assert self.find(Locators.LOGIN_FORM).is_displayed(), "Login form is missing"
        assert self.find(Locators.REGISTER_FORM).is_displayed(), "Registration form is missing"

    def register_new_user(self, email, password):
        self.find(Locators.EMAIL).send_keys(email)
        self.find(Locators.PASSWORD).send_keys(password)
        self.find(Locators.CONFIRM_PASSWORD).send_keys(password)
        self.find(Locators.SUBMIT).click()
