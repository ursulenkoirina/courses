import json
import pytest
import os
import allure

from data.random_string import random_string
from pages.pages import DashboardPage

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(file_dir, "..", "data", "status_data.json"), encoding="utf8") as f:
    status_text_list = json.load(f)

status_text_list.append(random_string(max_len=100))
# status_text_list.extend([random_string() for _ in range(5)])



@allure.feature('status feature')
@allure.story('Create status')
@pytest.mark.parametrize("input_text", status_text_list)
def test_create_status(driver, logged_user, input_text, db):
    dashboard_page = DashboardPage(driver)
    with allure.step(' Given initial amount of status in Oxwall database'):
        old_status_list = dashboard_page.status_elements
    with allure.step('When I add a status with {input_text} in Dashboard page'):
        dashboard_page.create_new_text_status(input_text)
        dashboard_page.wait_new_status_appear(old_status_list)
    # Verification
    with allure.step(' Then a new status block appears before old list of status'):
        assert db.get_last_text_status() == input_text
        new_status_element = dashboard_page.status_elements[0]
        with allure.step('Then this status block has this {input_text} and author as this user {logged_user} and time "within 1 minute"'):
            assert new_status_element.text == input_text
            assert new_status_element.user == logged_user

