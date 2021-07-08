import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")
    driver.maximize_window()

    print(driver.title)
    test_case1()


def test_case1():
    driver.find_element(By.XPATH, '//*[@id="save"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="save"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="save"]').click()


invoke_browser()
time.sleep(4)
driver.close()
