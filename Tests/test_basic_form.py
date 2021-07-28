from selenium import webdriver

from Pages.basic_forms_page import BasicForm
from Utils.locators import FormPageLocators
from Utils.test_data import Data
import time
from Utils.Logger import Logging

import allure
from allure_commons.types import AttachmentType


@allure.severity(allure.severity_level.NORMAL)
class Test_Form:
    logger = Logging.loggen()
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")

    @allure.severity(allure.severity_level.BLOCKER)
    def test_form(self):
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.logger.info("*************** Test_001_Form *****************")
        self.logger.info("*************** Form Test Started *****************")
        # open the driver
        obj = BasicForm(self.driver)
        # get the web page
        obj.open(FormPageLocators.FormUrl)
        time.sleep(3)
        # test form
        obj.input_numbers(Data.get_valid_number1(), Data.get_valid_number2())
        obj.click_total_button()
        self.logger.info("**** Form Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_form.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testForm", attachment_type=AttachmentType.PNG)
        # close browser

#pytest -v -s --alluredir=".\AllureReports" Tests\test_basic_form.py