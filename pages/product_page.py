from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BUTTON)
        basket_button.click()
    
    def check_added_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text
        assert product_name in added_product 

    def check_basket_value(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert book_price == basket_value

        # def should_be_login_link(self):
        #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

