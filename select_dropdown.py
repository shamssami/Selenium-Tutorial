import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
    driver.maximize_window()
    print(driver.title)


def select_list():
    week = driver.find_element(By.ID, "select-demo")
    day = Select(week)
    day.select_by_value("Sunday")
    time.sleep(6)


def multi_select_list():
    cars = driver.find_element(By.ID, "multi-select")
    car = Select(cars)
    car.select_by_value("Texas")
    driver.find_element(By.ID, "printMe").click()
    time.sleep(3)
    driver.find_element(By.ID, "printAll").click()
    time.sleep(6)


invoke_browser()
select_list()
multi_select_list()
driver.close()
