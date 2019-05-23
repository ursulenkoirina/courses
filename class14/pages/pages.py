from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from custom_expected_condition import presence_of_num_elements
from pages.elements import InputTextElement, StatusBlock

class OxwallApp:
    def __init__(self, driver, base_url="http://127.0.0.1/oxwall/"):
        self.driver = driver
        # # Open Oxwall site
        # self.driver.get(base_url)

        self.main_page = MainPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.sign_in_page = SignInPage(driver)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = webdriver.ActionChains(driver)

    def is_element_present(self, locator):
        try:
            el = self.driver.find_element(*locator)
        except NoSuchElementException as e:
            return False
        return el

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator),
                               message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                               message=f"Can't find elements by locator {locator}")

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator),
                               message=f"Can't find visible element by locator {locator}")

    def find_any_visible_elements(self, locator):
        return self.wait.until(EC.visibility_of_any_elements_located(locator),
                               message=f"Can't find any visible elements by locator {locator}")


class SignInPage(BasePage):
    SIGN_IN = (By.NAME, 'submit')
    USERNAME_INPUT = (By.NAME, 'identity')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_WINDOW_BOX = (By.CLASS_NAME, "floatbox_container")
    LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")
    # TODO: extract locators for other elements

    def is_this_page(self):
        return self.is_element_present(self.LOGIN_WINDOW_BOX)

    def sign_in_click(self):
        button = self.find_element(self.SIGN_IN)
        button.click()
        # TODO explain
        self.wait.until(EC.invisibility_of_element_located(self.LOGIN_BACKGROUND),
                        "Login background is still visible")
        return DashboardPage(self.driver)

    def input_password(self, user):
        # Input password
        passwd_field = self.find_element(self.PASSWORD_INPUT)
        passwd_field.send_keys(user.password)

    def input_username(self, user):
        # Input username
        username_field = self.find_element(self.USERNAME_INPUT)
        username_field.send_keys(user.username)


class InternalPage(BasePage):
    RIGHT_MENU_ELEMENTS = (By.CLASS_NAME, "ow_console_item")
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'ow_menu_wrap')]//li[contains(@class, 'active')]")
    # TODO: extract locators for other elements in logout

    @property
    def active_menu(self):
        return self.find_element(self.ACTIVE_MENU)

    def login_as(self, user):
        sign_in_page = self.sign_in_click()
        sign_in_page.input_username(user)
        sign_in_page.input_password(user)
        dashboard_page = sign_in_page.sign_in_click()
        return dashboard_page

    def sign_in_click(self):
        # Initialize login(click Sign in button)
        buttons = self.driver.find_elements(*self.RIGHT_MENU_ELEMENTS)
        buttons[0].click()
        return SignInPage(self.driver)

    def logout(self):
        # Logout
        driver = self.driver
        buttons = driver.find_elements_by_css_selector('.ow_console_item.ow_console_dropdown.ow_console_dropdown_hover')
        action = webdriver.ActionChains(driver)
        action.move_to_element(buttons[0]).perform()
        action.move_to_element(driver.find_element_by_link_text('Sign Out')).click().perform()


class MainPage(InternalPage):
    # TODO: structure and action on Main Page
    pass


class DashboardPage(InternalPage):
    STATUS_INPUT_FIELD = (By.NAME, 'status')
    USER_MENU = (By.CSS_SELECTOR, '.ow_console_item.ow_console_dropdown:nth-child(5) > a')
    SEND_BUTTON =(By.NAME, "save")
    STATUS_BLOCK = (By.XPATH, "//li[contains(@id, 'action-feed')]")
    STATUS_USER = (By.CLASS_NAME, 'ow_newsfeed_string')

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.STATUS_INPUT_FIELD = (By.NAME, 'status')
    #     self.status_input_field = self.wait.until(EC.presence_of_element_located(self.STATUS_INPUT_FIELD))
    #     self.send_button = self.driver.find_element(*self.SEND_BUTTON)
    #     self.status_text_elements = self.driver.find_elements(*self.STATUS_BLOCK)

    @property
    def status_input_field(self):
        return InputTextElement(self.find_visible_element(self.STATUS_INPUT_FIELD))

    @property
    def send_button(self): return self.find_element(self.SEND_BUTTON)

    @property
    def status_elements(self):
        return [StatusBlock(item) for item in self.find_elements(self.STATUS_BLOCK)]

    @property
    def user_status_elements(self):
        return self.find_elements(self.STATUS_USER)

    def user_menu_present(self):
        return self.is_element_present(self.USER_MENU)

    def create_new_text_status(self, input_text):
        # Enter new status text
        self.status_input_field.input(input_text)
        # Submit new status
        self.send_button.click()

    def wait_new_status_appear(self, old_list_of_elements):
        # Wait until new status appears
        new_num = len(old_list_of_elements) + 1
        status_text_elements = self.wait.until(presence_of_num_elements(self.STATUS_BLOCK, new_num))
        return status_text_elements[0]


if __name__ == "__main__":
    driver = webdriver.Chrome()
    m = MainPage(driver)
    print(m.__str__())
