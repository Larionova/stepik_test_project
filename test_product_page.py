import time
import pytest
import random
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        self.login_page.register_new_user(BasePage.registration_email(), BasePage.registration_password())
        self.login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.click_on_button_add_in_basket()
        self.product_page.product_in_basket()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        self.product_page = ProductPage(browser, link)
        self.product_page.open()
        self.product_page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('promo', [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='Bug in the page'))
                                   for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_button_add_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_in_basket()


@pytest.mark.xfail(reason="there is a message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_button_add_in_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail(reason="not disappiring")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_button_add_in_basket()
    product_page.should_be_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_basket_empty()
    page_basket.should_be_in_basket_message_empty()
