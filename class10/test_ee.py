from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def test_create_status(driver):
    input_text = 'AAAAAA'
    driver.find_element_by_class_name('status').send_keys(input_text)
    driver.find_element_by_class_name('save').click()
    sleep(5)
    # el =(driver.find_element...)
    # assert el.text == input_text






