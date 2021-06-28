from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form') 

class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADDED_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    BASKET_VALUE = (By.CSS_SELECTOR, 'div.alert p > strong')
    BOOK_PRICE = (By.CSS_SELECTOR,'p.price_color')