from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_in_basket(self):
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
    def should_be_message(self):
