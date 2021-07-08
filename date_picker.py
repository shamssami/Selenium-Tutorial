import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from datetime import datetime

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    driver.maximize_window()
    print(driver.title)
    test_case1()


def test_case1():
    # click on date_picker to select a date
    driver.find_element(By.CSS_SELECTOR, "#sandbox-container1 > div > input").click()
    # click on Today
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tfoot/tr[1]/th").click()
    time.sleep(6)
    # After click on today we want to clear it so click again on date picker
    driver.find_element(By.CSS_SELECTOR, "#sandbox-container1 > div > input").click()
    # click on clear
    driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tfoot/tr[2]/th").click()


def test_case2():
    current_date = datetime.date().today()
    future_date = current_date.day()+1
    f_date = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[4]").get_attribute()
    future_date = datetime.date().strftime("%d/%m/%Y")
    print(future_date)

    if current_date > future_date:
        print("Date missed")
    else:
        print("You cant select future date :)")


invoke_browser()
time.sleep(5)
driver.close()
