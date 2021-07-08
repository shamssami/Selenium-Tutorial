import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    driver.maximize_window()
    print(driver.title)
    single_input_field()
    time.sleep(2)
    two_input_fields()


def single_input_field():
    driver.find_element_by_id("user-message").send_keys("Hello World!")
    driver.find_element_by_css_selector("#get-input > button").click()
    time.sleep(4)


def two_input_fields():
    driver.find_element_by_id("sum1").send_keys(1)
    driver.find_element_by_id("sum2").send_keys(2)

    driver.find_element_by_css_selector("#gettotal > button").click()


invoke_browser()
time.sleep(3)
driver.close()
