import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/jquery-dual-list-box-demo.html")
    driver.maximize_window()
    print(driver.title)
    pick_list()


def pick_list():
    selections = driver.find_element(By.XPATH, '//*[@id="pickList"]/div/div[1]/select')
    selection = Select(selections)
    selection.select_by_index(2)
    # add value for other list
    driver.find_element(By.XPATH, '//*[@id="pickList"]/div/div[2]/button[1]').click()
    selection.select_by_index(3)
    # add another value for other list
    driver.find_element(By.XPATH, '//*[@id="pickList"]/div/div[2]/button[1]').click()
    selection.select_by_index(4)
    # add another value for other list
    driver.find_element(By.XPATH, '//*[@id="pickList"]/div/div[2]/button[1]').click()
    time.sleep(4)
    # remove all items
    driver.find_element(By.XPATH, '//*[@id="pickList"]/div/div[2]/button[4]').click()
    time.sleep(2)
    #  click on addAll button
    driver.find_element(By.XPATH, '//*[@id="pickList"]/div/div[2]/button[2]').click()
    time.sleep(2)


invoke_browser()
driver.close()
