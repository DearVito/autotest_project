import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language.")
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose your browser (default is Chrome).")


@pytest.fixture(scope="function")
def browser(request):
    browser_name_is = request.config.getoption("browser_name")
    selected_language = request.config.getoption("language")
    
    if browser_name_is == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs',{'intl.accept_languages':selected_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name_is == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages",selected_language)
        browser = webdriver.Firefox(firefox_profile = fp)

    yield browser
    print("\nquit browser..")
    browser.quit()