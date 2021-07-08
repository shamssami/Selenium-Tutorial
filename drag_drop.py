import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
    driver.maximize_window()

    print(driver.title)


def test_case1():
    driver.find_element(By.XPATH, '//*[@id="todrag"]/span[1]').click()
    source = driver.find_element(By.XPATH, '//*[@id="todrag"]/span[1]')
    target = driver.find_element(By.XPATH, '//*[@id="mydropzone"]')
    # action chain object creation
    action = ActionChains(driver)
    # drag and drop operation and the perform
    action.drag_and_drop(source, target).perform()
    time.sleep(3)
    dropped_list = list(driver.find_element_by_id("droppedlist").find_elements_by_tag_name("span"))
    for i in dropped_list:
        print(i.text)


invoke_browser()
test_case1()
time.sleep(6)
driver.close()
