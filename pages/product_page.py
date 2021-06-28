from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON)
        basket_button.click()
    
    def check_added_product_name(self):
        assert "The shellcoder's handbook" in self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text

    def check_basket_value(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert book_price == basket_value

        # def should_be_login_link(self):
        #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

