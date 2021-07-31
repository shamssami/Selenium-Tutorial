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

    @allure.severity(allure.severity_level.BLOCKER)
    def test_input_form(self, test_setup):
        self.driver = test_setup
        self.driver.get(InputFormLocators.InputFormUrl)

        self.obj = InputForm(self.driver)
        self.logger.info("*************** Test_001_Fill_Form *****************")

        # get the web page
        self.logger.info("*************** Fill Form Test Started *****************")

        time.sleep(3)
        # test form
        self.obj.input_data()

        count = 0
        if self.obj.check_invalidation() is True:
            count = count + 1
            print("Test Failed with ", count, "errors")

        self.logger.info("**** Fill Form Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\screenshots\\" + "test_input_form.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testInputForm", attachment_type=AttachmentType.PNG)

        # close browser
        self.driver.close()

# pytest -v -s --alluredir=".\AllureReports" Tests\test_input_form.py
# pytest -v --html=PytestReports\inputform_report.html Tests\test_input_form.py
