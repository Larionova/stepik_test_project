from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_in_basket(self):
        self.should_be_book_name()
        self.should_be_book_price()
        self.should_not_be_success_message()
        self.should_be_disappear()

    def click_on_button_add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), 'Button is not presented'
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_backet = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_backet, "Name book is different"

    def should_be_book_price(self):
        price_book = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_backet = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert price_book == price_backet, "Price book is different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
