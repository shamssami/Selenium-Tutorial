#
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
    driver.maximize_window()
    print(driver.title)


def test_case1():
    # first_name
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > "
                                         "div:nth-child(2) > div > div > input").send_keys("Shams")
    # last_name
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > "
                                         "div:nth-child(3) > div > div > input").send_keys("Salman")
    # email
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > "
                                         "div:nth-child(4) > div > div > input").send_keys("2018@bethlehem.edu")

    # phone
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > "
                                         "div:nth-child(5) > div > div > input").send_keys("9874563210")
    # address
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(6) > div > div > input").send_keys(
        "Anchorage")
    # city
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(7) > div > div > input").send_keys(
        "Anchorage")

    # state --> invoke the method to select the state
    select_state()

    # zip code

    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(9) > div > div > input").send_keys(
        "99508")
    # website domain name
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(10) > div > div > input").send_keys(
        "shams.com")
    # Click on No radio button
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(11) > div > "
                                         "div:nth-child(2) > label > input[type=radio]").click()

    # project description
    driver.find_element(By.CSS_SELECTOR,
                        "#contact_form > fieldset > div:nth-child(12) > div > div > textarea").send_keys(
        "The project is great!")

    # submit the form
    driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(14) > div > button").click()
    time.sleep(6)


def select_state():
    states = driver.find_element(By.CSS_SELECTOR, "#contact_form > fieldset > div:nth-child(8) > div > div > select")
    state = Select(states)
    state.select_by_index(2)
    time.sleep(2)


invoke_browser()
test_case1()
driver.close()
