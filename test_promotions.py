import pytest

from pages.product_page import ProductPage


CATALOG = "https://selenium1py.pythonanywhere.com/catalogue/"
SHELLCODER = CATALOG + "the-shellcoders-handbook_209/"
CODERS = CATALOG + "coders-at-work_207/"
BUGGED_OFFER = pytest.param(
    7,
    marks=pytest.mark.xfail(reason="Wrong product title", raises=AssertionError, strict=True),
)


@pytest.mark.parametrize(
    "url",
    [SHELLCODER + "?promo=newYear", CODERS + "?promo=newYear2019"],
    ids=["newYear", "newYear2019"],
)
def test_holiday_promo(browser, url):
    check_basket_after_promo(browser, url)


@pytest.mark.parametrize("offer", [0, 1, 2, 3, 4, 5, 6, BUGGED_OFFER, 8, 9])
def test_promo_offer(browser, offer):
    check_basket_after_promo(browser, f"{CODERS}?promo=offer{offer}")


def check_basket_after_promo(browser, url):
    page = ProductPage(browser, url)
    page.open()
    title = page.product_title()
    price = page.product_price()
    page.add_product_to_basket()
    page.solve_promo_quiz()
    page.should_show_added_product(title)
    page.should_show_correct_basket_total(price)
