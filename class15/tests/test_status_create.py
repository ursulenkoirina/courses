import json
import pytest
import os

from data.random_string import random_string
from pages.pages import DashboardPage

file_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(file_dir, "..", "data", "status_data.json"), encoding="utf8") as f:
    status_text_list = json.load(f)

status_text_list.append(random_string(max_len=100))
# status_text_list.extend([random_string() for _ in range(5)])


@pytest.mark.parametrize("input_text", status_text_list)
def test_create_status(driver, logged_user, input_text, db):
    dashboard_page = DashboardPage(driver)
    # Locate existed text statuses
    old_status_list = dashboard_page.status_elements
    # Create new status
    assert dashboard_page.status_input_field.placeholder == "What’s happening?"
    dashboard_page.create_new_text_status(input_text)
    dashboard_page.wait_new_status_appear(old_status_list)
    # Verification
    assert db.get_last_text_status() == input_text
    new_status_element = dashboard_page.status_elements[0]
    assert new_status_element.text == input_text
    assert new_status_element.user == logged_user
