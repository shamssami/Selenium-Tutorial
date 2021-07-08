import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
    driver.maximize_window()
    print(driver.title)


def date_fields():
    driver.find_element(By.CSS_SELECTOR, "#datepicker > input:nth-child(1)").click()
    # 8
    sunday = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[5]")
    sunday.click()
    x1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[5]").get_attribute("class")
    print(x1)
    time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, "#datepicker > input:nth-child(3)").click()
    x2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[5]").get_attribute("class")
    print(x2)
    if x1 in x2:
        print("The Two fields have same date")


def compare_dates():
    driver.find_element(By.CSS_SELECTOR, "#datepicker > input:nth-child(1)").click()
    sunday = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[5]")
    sunday.click()
    x1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[5]").text
    print(x1)
    driver.find_element(By.CSS_SELECTOR, "#datepicker > input:nth-child(3)").click()
    x2 = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/table/tbody/tr[2]/td[6]").text
    print(x2)
    if x1 < x2:
        print("Test Passed")


invoke_browser()
date_fields()
compare_dates()
driver.close()
