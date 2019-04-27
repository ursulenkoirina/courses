import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.keys import Keys
from app_helper import OxwallApp
from modules.user import User

@pytest.fixture()
def driver():
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return OxwallApp(driver, base_url="https://127.0.0.1/oxwall/")
    # return OxwallApp(driver,base_url="https://demo.oxwall.com/")



@pytest.fixture()
def logged_user(app):
    # user = User(username='demo', password='demo', real_name='Demo')
    user = User(username='admin', password='password', real_name='Admin')
    # app.login_as(username='demo', password='demo')
    app.login_as(user)
    yield user
    app.logout()





