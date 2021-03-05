import time
import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ['?promo=offer0', '?promo=offer1', '?promo=offer2', '?promo=offer3', '?promo=offer4',
                                   '?promo=offer5', '?promo=offer6', '?promo=offer7', '?promo=offer8', '?promo=offer9'])
@pytest.mark.xfail(reason='wrong message')
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_on_button_add_in_basket()
    product_page.solve_quiz_and_get_code()
    product_page.product_in_basket()
    # time.sleep(120)
