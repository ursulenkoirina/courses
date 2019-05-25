from pytest_bdd import given, when, then

from models.user import User
from pages.pages import DashboardPage


@given("initial amount of status in Oxwall database")
def initial_statuses(app):
    return app.dashboard_page.status_elements


@given("I as a logged user")
def logged_user(app, config):
    user = User(**config["web"], is_admin=True)
    app.main_page.login_as(user)
    return user


@when("I add a status with <text> in Dashboard page")
def create_status(driver, text):
    dashboard_page = DashboardPage(driver)
    dashboard_page.create_new_text_status(text)


@then("a new status block appears before old list of status")
def new_status_block_appears(app, initial_statuses):
    app.dashboard_page.wait_new_status_appear(initial_statuses)


@then('this status block has this <text> and author as this user and time "within 1 minute"')
def check_status_data(app, text, logged_user):
    new_status_element = app.dashboard_page.status_elements[0]
    assert new_status_element.text == text
    assert new_status_element.user == logged_user
    assert new_status_element.time == "within 1 minute"




