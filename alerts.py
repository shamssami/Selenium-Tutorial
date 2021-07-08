import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html")
    driver.maximize_window()
    print(driver.title)
    alert_test()


def alert_test():
    # Add all buttons in a list
    l = list(driver.find_elements(By.TAG_NAME, 'button'))
    # check if the button display normal/auto closeable message
    for i in l:
        if "Autocloseable" in i.text:
            i.click()
            time.sleep(5)
        elif "Normal" in i.text:
            i.click()

    # close all normal closeable messages
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[4]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[6]/button').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[8]/button').click()


invoke_browser()
time.sleep(5)
driver.close()
