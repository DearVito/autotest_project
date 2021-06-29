from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_books_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_IN_BASKET), "Book is presented, but should not be"
    
    def basket_is_empty_message(self):
        message_about_books_in_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert ('Ваша корзина пуста' in message_about_books_in_basket or 'Your basket is empty' in message_about_books_in_basket)

