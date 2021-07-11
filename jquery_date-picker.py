import datetime
import time
from datetime import datetime
from datetime import timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/jquery-date-picker-demo.html")
    driver.maximize_window()
    print(driver.title)


def pick_dates():
    driver.find_element(By.ID, "from").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/table/tbody/tr[2]/td[5]/a").click()
    time.sleep(3)
    driver.find_element(By.ID, "to").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#ui-datepicker-div > table > tbody > tr:nth-child(3) > td:nth-child(5) > a").click()
    time.sleep(6)
    driver.find_element(By.ID, "from").clear()
    driver.find_element(By.ID, "to").clear()


# this method is for sending the date using send_keys() into the text field
def input_date():
    driver.find_element(By.ID, "from").send_keys("07/07/2021")
    time.sleep(3)
    driver.find_element(By.ID, "to").send_keys("07/07/2021")
    from_date = driver.find_element(By.ID, "from").get_attribute("value")
    to_date = driver.find_element(By.ID, "to").get_attribute("value")
    if from_date <= to_date:
        print("Test is passed ")
    else:
        print("from_date should be less than to_date!")


invoke_browser()
pick_dates()

input_date()

time.sleep(3)
driver.close()
