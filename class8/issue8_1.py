import time
from selenium import webdriver
driver = webdriver.Firefox(
    executable_path='/usr/local/bin/geckodriver'
)
# driver = webdriver.Chrome(
#     executable_path='/usr/local/bin/chromedriver'
# )
driver.get('http://google.com')
# a = driver.find_elements_by_partial_link_text('Tu')
# time.sleep(10)
# print(a)

# driver.find_element_by_class_name('gb_Td').click()
# driver.close()
