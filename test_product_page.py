from .pages.product_page import ProductPage
import time

def test_guest_can_go_to_login_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_added_product_name()
    page.check_basket_value()
    time.sleep(1)

    
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()

    # def test_guest_should_see_login_link(browser): 
    #     link = "http://selenium1py.pythonanywhere.com/"
    #     page = MainPage(browser,link)
    #     page.open()
    #     page.should_be_login_link()
    