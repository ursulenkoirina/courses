import pytest
from selenium import webdriver
from app_helper import OxwallApp


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    # return OxwallApp(driver, base_url="http://127.0.0.1/oxwall/")
    return OxwallApp(driver, base_url="https://demo.oxwall.com/")

@pytest.fixture()
def session(app):
    # app.login_as(username='admin', password='pass')
    app.login_as(username='demo', password='demo')
    yield
    app.logout()



