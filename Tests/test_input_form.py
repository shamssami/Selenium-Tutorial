import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.input_form import InputForm
from Utils.locators import InputFormLocators
import time
from Utils.Logger import Logging


@allure.severity(allure.severity_level.NORMAL)
class Test_InputForm:
    logger = Logging.loggen()
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")

    @allure.severity(allure.severity_level.BLOCKER)
    def test_input_form(self):

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()        # open the driver
        obj = InputForm(self.driver)
        self.logger.info("*************** Test_001_Fill_Form *****************")

        # get the web page
        obj.open(InputFormLocators.InputFormUrl)
        self.logger.info("*************** Fill Form Test Started *****************")

        time.sleep(3)
        # test form
        obj.input_data()

        count = 0
        if obj.check_invalidation() is True:
            count = count + 1
            print("Test Failed with ", count, "errors")

        self.logger.info("**** Fill Form Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\screenshots\\" + "test_input_form.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testInputForm", attachment_type=AttachmentType.PNG)

        # close browser
        self.driver.close()


#pytest -v -s --alluredir=".\AllureReports" Tests\test_input_form.py
# pytest -v --html=PytestReports\inputform_report.html Tests\test_input_form.py