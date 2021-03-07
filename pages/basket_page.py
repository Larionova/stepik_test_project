from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), 'Product in basket'

    def should_be_in_basket_message_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE_EMPTY), 'Basket is not empty'
