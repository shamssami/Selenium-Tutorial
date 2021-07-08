import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
    driver.maximize_window()
    print(driver.title)
    single_checkbox()
    time.sleep(2)
    multiple_checkbox()


def single_checkbox():
    driver.find_element_by_id("isAgeSelected").click()


def multiple_checkbox():
    driver.find_element_by_id("check1").click()
    time.sleep(5)
    driver.find_element_by_css_selector("#easycont > div > div.col-md-6.text-left > "
                                        "div:nth-child(5) > div.panel-body > div:nth-child(3) > label > input").click()

    time.sleep(3)


invoke_browser()
driver.close()
