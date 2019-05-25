import json
import os

import pytest
from selenium import webdriver

from db_connector import OxwallDB
from pages.pages import MainPage, OxwallApp
from models.user import User

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="config file")
    parser.addoption("--browser", action="store", default="Chrome",
                     help="browser")


@pytest.fixture()
def driver(request):
    # browser = request.config.getoption("--browser")
    # if browser == "Chrome":
    #     driver = webdriver.Chrome()
    # elif browser == "Firefox":
    #     driver = webdriver.Firefox()
    # else:
    #     driver = webdriver.Chrome()
    # driver = selenium
    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def config(request):
    file_name = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, file_name)) as f:
        return json.load(f)

@pytest.fixture(autouse=True)
def app(driver, base_url):
    driver.get(base_url)
    return OxwallApp(driver)


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(config["db"])
    yield db
    db.close()


with open(os.path.join(PROJECT_DIR, "data", "user_data.json"), encoding="utf8") as f:
    user_data_list = json.load(f)


@pytest.fixture(params=user_data_list, ids=[str(user) for user in user_data_list])
def user(request, db):
    user = User(**request.param)
    db.create_user(user)
    yield user
    db.delete_user(user)


@pytest.fixture()
def logged_user(driver, config):
    user = User(**config["web"], is_admin=True)
    main_page = MainPage(driver)
    main_page.login_as(user)
    yield user
    main_page.logout()
