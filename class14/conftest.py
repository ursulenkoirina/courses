import json
import os

import pytest
from selenium import webdriver

from db_connector import OxwallDB
from pages.pages import MainPage, OxwallApp
from models.user import User


@pytest.fixture()
def driver():
    # driver = selenium
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def app(driver):
    base_url = "http://127.0.0.1/oxwall/"
    driver.get(base_url)
    return OxwallApp(driver)


@pytest.fixture(scope="session")
def db():
    db = OxwallDB()
    yield db
    db.close()


project_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(project_dir, "data", "user_data.json"), encoding="utf8") as f:
    user_data_list = json.load(f)


@pytest.fixture(params=user_data_list, ids=[str(user) for user in user_data_list])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)


@pytest.fixture()
def logged_user(driver):
    user = User(username='admin', password='password', real_name="Admin")
    main_page = MainPage(driver)
    main_page.login_as(user)
    yield user
    main_page.logout()
