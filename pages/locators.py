from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form') 

class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADDED_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_VALUE = (By.CSS_SELECTOR, 'div.alert p > strong')
    BOOK_PRICE = (By.CSS_SELECTOR,'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    SUCCESS_MESSAGE = (By.XPATH,'//*[@id="messages"]/div[1]/div')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
