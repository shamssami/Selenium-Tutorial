from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def setup():
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


def close():
    driver.close()
