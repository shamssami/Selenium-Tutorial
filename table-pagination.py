#
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/table-pagination-demo.html")
    driver.maximize_window()
    print(driver.title)
    test_case()


def test_case():
    rows = len(driver.find_elements(By.XPATH, '//*[@id="myTable"]/tr'))
    print("Total No of rows in the table is: ", rows)
    # page1
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[2]/a').click()

    page1 = list(driver.find_elements(By.XPATH, '//*[@id="myTable"]/tr'))
    count1 = 0
    for i in page1:
        if i.get_attribute("style") == "display: table-row;":
            count1 += 1
    print("Total No of records for page1 is: ", count1)

    # page2
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[3]/a').click()
    page2 = list(driver.find_elements(By.XPATH, '//*[@id="myTable"]/tr'))
    count2 = 0
    for i in page2:
        if i.get_attribute("style") == "display: table-row;":
            count2 += 1
    print("Total No of records for page1 is: ", count2)

    # page3
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[4]/a').click()
    page3 = list(driver.find_elements(By.XPATH, '//*[@id="myTable"]/tr'))
    count3 = 0
    for i in page3:
        if i.get_attribute("style") == "display: table-row;":
            count3 += 1
    print("Total No of records for page1 is: ", count3)


# Second Page will have both Prev and Next buttons enabled to navigate

def navigation_page2():
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[3]/a').click()
    driver.find_element(By.XPATH, '//*[@id="myPager"]/li[5]/a').click()
    print("Navigation is valid")


invoke_browser()
time.sleep(3)
navigation_page2()
driver.close()
