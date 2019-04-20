import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def session(driver):
    base_url = 'https://demo.oxwall.com/'
    driver.get(base_url)

    class presents_of_num_elements:
        def __init__(self, locator, number):
            self.locator = locator
            self.number = number

        def __call__(self, driver):
            els = driver.find_elements(*self.locator)
            if len(els) == self.number:
                return els

    wait = WebDriverWait(driver, 10)
    buttons = wait.until(presents_of_num_elements((By.CLASS_NAME, 'ow_console_item'), 2))
    buttons[0].click()
    # name = driver.find_element_by_name('identity')
    # name.send_keys('demo')
    # password = driver.find_element_by_name('password')
    # password.send_keys('demo')
    sign_in_but = driver.find_element_by_class_name('ow_positive')
    sign_in_but.click()
    buttons = driver.find_elements_by_css_selector('.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
    action = ActionChains(driver)
    action.move_to_element(buttons[0]).perform()
    action.move_to_element(driver.find_element_by_link_text('Sign Out')).click().perform()

