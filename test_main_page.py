from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


HOME = "https://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, HOME)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, HOME)
    page.open()
    page.go_to_login_page()
    LoginPage(browser, browser.current_url).should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, HOME)
    page.open()
    page.go_to_basket()
    BasketPage(browser, browser.current_url).should_be_empty()
