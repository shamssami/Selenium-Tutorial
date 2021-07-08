import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/data-list-filter-demo.html")
    driver.maximize_window()
    print(driver.title)
    test_case1()


def test_case1():
    # filter by name
    driver.find_element(By.XPATH, '//*[@id="input-search"]').send_keys("Tyreese Burn")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="input-search"]').clear()
    # filter by Title
    driver.find_element(By.XPATH, '//*[@id="input-search"]').send_keys("Manager")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="input-search"]').clear()
    # filter by phone No
    driver.find_element(By.XPATH, '//*[@id="input-search"]').send_keys("644-555-2222")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="input-search"]').clear()
    # filter by phone No
    driver.find_element(By.XPATH, '//*[@id="input-search"]').send_keys("test3@company.com")
    print("Test sucess by filtering existing data ")
    # Not Existing data filter
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="input-search"]').clear()
    # filter by phone No
    driver.find_element(By.XPATH, '//*[@id="input-search"]').send_keys("Shams Salman")


invoke_browser()
time.sleep(4)
driver.close()
