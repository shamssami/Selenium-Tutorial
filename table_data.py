#
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
    driver.maximize_window()
    print(driver.title)
    filter_data()


# Type in your search to filter data by Tasks / Assignee / Status

def filter_data():
    # filter by task
    driver.find_element(By.XPATH, '//*[@id="task-table-filter"]').send_keys("Wireframes")
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="task-table-filter"]').clear()
    # filter by Assignee
    driver.find_element(By.XPATH, '//*[@id="task-table-filter"]').send_keys("Mike Trout	")
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="task-table-filter"]').clear()
    # filter by Status
    driver.find_element(By.XPATH, '//*[@id="task-table-filter"]').send_keys("in progress")
    time.sleep(4)


# Click the filter icon to activate column filters inputs ()

def test_filter():
    # column filter inputs are disabled before clicking on filter icon
    print("Enable status of filter input before Activation the filter icon: ", driver.find_element(By.XPATH,
                                                                                                   '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input').is_enabled())
    # click on filter icon
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div/div/button').click()
    time.sleep(2)
    # Activate column filter inputs
    print("Enable status of filter input before Activation the filter icon: ", driver.find_element(By.XPATH,
                                                                                                   '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input').is_enabled())
    time.sleep(2)


invoke_browser()
test_filter()
driver.close()
