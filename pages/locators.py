from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'form#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'form#register_form') 
    REGISTRATION_EMAIL = (By.CSS_SELECTOR,'input#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR,'input#id_registration-password1')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR,'input#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR,"button[value='Register']")

class ProductPageLocators():
    BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADDED_PRODUCT = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BASKET_VALUE = (By.CSS_SELECTOR, 'div.alert p > strong')
    BOOK_PRICE = (By.CSS_SELECTOR,'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    SUCCESS_MESSAGE = (By.XPATH,'//*[@id="messages"]/div[1]/div')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR,'div#content_inner p')
    BOOK_IN_BASKET = (By.CSS_SELECTOR,'img.thumbnail')

    
