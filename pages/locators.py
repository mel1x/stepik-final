from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    SUBMIT = (By.CSS_SELECTOR, "#register_form button[type='submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_TITLE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")


class BasketPageLocators:
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    SUMMARY = (By.ID, "content_inner")
