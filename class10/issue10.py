import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome(
#     executable_path='/usr/local/bin/chromedriver'
# )
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://novaposhta.ua/')
el = driver.find_element_by_class_name('logo_in')
action = webdriver.ActionChains(driver)
action.key_down(Keys.CONTROL)
action.click(el)
action.key_up(Keys.CONTROL)
action.perform()


all_windows = driver.window_handles
print(all_windows)
this_window = driver.current_window_handle
print(this_window)
driver.switch_to.window(driver.window_handles[1])
# el.click()
