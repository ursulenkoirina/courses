from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
base_url ='https://demo.oxwall.com/'
driver.get(base_url)
# sign_in_but = driver.find_element_by_class_name('ow_console_item')


# def presents_of_2_elements(driver):
#     els = driver.find_elements_by_class_name('ow_console_item')
#     print(len(els))
#     if len(els) == 2:
#         return els
#
#
# wait = WebDriverWait(driver, 10)
# buttons = wait.until(presents_of_2_elements)
# buttons[1].click()


# def presents_of_num_elements(number):
#     def func(driver):
#         els = driver.find_elements_by_class_name('ow_console_item')
#         if len(els) == number:
#             return els
#     return func
#
#
# wait = WebDriverWait(driver, 10)
# buttons = wait.until(presents_of_num_elements(2))
# buttons[1].click()

class presents_of_num_elements:
    def __init__(self, locator,number):
        self.locator = locator
        self.number = number
    def __call__(self, driver):
        els = driver.find_elements(*self.locator)
        if len(els) == self.number:
            return els


wait = WebDriverWait(driver, 10)
driver.save_screenshot('1.png')
buttons = wait.until(presents_of_num_elements((By.CLASS_NAME,'ow_console_item'),2))
buttons[1].click()
