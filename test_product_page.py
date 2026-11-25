from uuid import uuid4

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


PRODUCT = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT)
    page.open()
    title = page.product_title()
    price = page.product_price()
    page.add_product_to_basket()
    page.should_show_added_product(title)
    page.should_show_correct_basket_total(price)


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT)
    page.open()
    page.go_to_basket()
    BasketPage(browser, browser.current_url).should_be_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT)
    page.open()
    page.go_to_login_page()
    LoginPage(browser, browser.current_url).should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login = LoginPage(browser, "https://selenium1py.pythonanywhere.com/accounts/login/")
        login.open()
        login.register_new_user(f"test-{uuid4().hex}@example.com", f"Pw-{uuid4().hex}!")
        login.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT)
        page.open()
        title = page.product_title()
        price = page.product_price()
        page.add_product_to_basket()
        page.should_show_added_product(title)
        page.should_show_correct_basket_total(price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT)
        page.open()
        page.should_not_show_success_message()


@pytest.mark.xfail(reason="The store shows a success message after adding the product", raises=AssertionError)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT)
    page.open()
    page.add_product_to_basket()
    page.should_not_show_success_message()


@pytest.mark.xfail(reason="The success message remains on the page", raises=AssertionError)
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT)
    page.open()
    page.add_product_to_basket()
    page.should_hide_success_message()
