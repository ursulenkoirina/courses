import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from custom_expected_condition import presence_of_num_elements


class OxwallApp:
    def __init__(self, driver, base_url="https://demo.oxwall.com/"):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Open oxfewll site
        self.driver.get(base_url)

    def is_element_present(self, how, what):
        # try:
        #     self.driver.find_element(by=how, value=what)
        # except NoSuchElementException as e:
        #     return False
        # return True
        els = self.driver.find_elements(by=how, value=what)
        if len(els)==0:
            return False
        else:
            return els

    def is_user_menu_present(self):
        return self.is_element_present(By.CSS_SELECTOR,'.ow_console_item.ow_console_dropdown >a')

    def status_text_elements(self):
        return self.driver.find_elements_by_class_name('ow_newsfeed_content')

    def user_of_new_status_elements(self):
        return self.driver.find_elements_by_class_name('ow_newsfeed_string')

    def logout(self):
        # Logout
        driver = self.driver
        buttons = driver.find_elements_by_css_selector('.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
        action = webdriver.ActionChains(driver)
        action.move_to_element(buttons[0]).perform()
        action.move_to_element(driver.find_element_by_link_text('Sign Out')).click().perform()


    def login_as(self, user):
        driver = self.driver
        # Initialize login(click sign in button)
        button = driver.find_elements_by_class_name("ow_console_item")
        button[0].click()
        # Input username
        username_field = driver.find_element_by_name("identity")
        username_field.clear()
        username_field.send_keys(user.username)
        # Input username
        passwd = driver.find_element_by_name('password')
        passwd.clear()
        passwd.send_keys(user.password)
        # Sign in
        button = driver.find_element_by_name('submit')
        button.click()


    def create_new_text_status(self, input_text):
        driver = self.driver
        # Enter new status text
        status_input_field = self.wait.until(EC.presence_of_element_located((By.NAME, 'status')))
        status_input_field.send_keys(input_text)
        # Submit new status
        driver.find_element_by_name('save').click()

    def wait_new_status_appear(self, old_list_of_elements):
        # Wait until new status appears
        new_num = len(old_list_of_elements) + 1
        status_text_elements = self.wait.until(presence_of_num_elements((By.CLASS_NAME, 'ow_newsfeed_content'), new_num))
        return status_text_elements[0]
