import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/table-sort-search-demo.html")
    driver.maximize_window()
    print(driver.title)
    driver.implicitly_wait(3)


def filter_test():
    driver.find_element(By.XPATH, '//*[@id="example_filter"]/label/input').send_keys("New York")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="example_filter"]/label/input').send_keys("London")
    time.sleep(3)


def sort_test():
    # sort By Name DESC
    driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr/th[1]').click()
    time.sleep(2)
    # Sort By Position DESC
    driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr/th[2]').click()
    time.sleep(2)
    # Sort By Office DESC
    driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr/th[3]').click()
    time.sleep(2)

    # Sort By Age DESC
    driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr/th[4]').click()
    time.sleep(2)
    # Sort By start date DESC
    driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr/th[5]').click()
    time.sleep(2)
    # Sort By salary DESC
    driver.find_element(By.XPATH, '//*[@id="example"]/thead/tr/th[6]').click()
    time.sleep(2)


invoke_browser()
filter_test()
sort_test()
driver.close()
