import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/bootstrap-modal-demo.html")
    driver.maximize_window()
    print(driver.title)
    single_modal()
    time.sleep(3)


def single_modal():
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/div/div[2]/a').click()
    time.sleep(2)

    print(driver.find_element(By.XPATH, '//*[@id="myModal0"]/div/div/div[3]').text)
    print("clicked on: " + driver.find_element(By.XPATH, '//*[@id="myModal0"]/div/div/div[4]/a[2]').text)
    driver.find_element(By.XPATH, '//*[@id="myModal0"]/div/div/div[4]/a[2]').click()


def multiple_modals_case1():
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[3]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="myModal2"]/div/div/div[6]/a[2]').click()


def multiple_modals_case2():
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[3]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="myModal2"]/div/div/div[6]/a[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[4]/a[2]').click()


invoke_browser()
multiple_modals_case1()
time.sleep(2)
multiple_modals_case2()
time.sleep(2)
driver.close()
