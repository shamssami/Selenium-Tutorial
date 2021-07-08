import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")


def invoke_browser():
    driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
    driver.maximize_window()
    print(driver.title)
    download_dialog()


# The progress bar is designed to display the current percent
# complete for a process after clicking on 'Start Download' button

def download_dialog():
    # Click below button to start download.
    driver.find_element(By.XPATH, '//*[@id="downloadButton"]').click()
    time.sleep(11)

    print("is 'Complete!' displayed?  ", driver.find_element(By.XPATH, '//*[@id="dialog"]/div[1]').is_displayed())


# Stylish progress bar demo for the automation
# When you click download , progress bar with percentage will be displayed.


def progress_bar_download():
    driver.get("https://www.seleniumeasy.com/test/bootstrap-download-progress-demo.html")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="cricle-btn"]').click()
    time.sleep(10)
    while driver.find_element(By.XPATH, '//*[@id="circle"]/div/div[1]').text != '100%':
        print(driver.find_element(By.XPATH, '//*[@id="circle"]/div/div[1]').text)


invoke_browser()
progress_bar_download()
driver.close()
