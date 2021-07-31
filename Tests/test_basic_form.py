
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

    ##################
    @allure.severity(allure.severity_level.BLOCKER)
    def test_input_form(self, test_setup):
        self.logger.info("*************** Test_001_Calculation *****************")
        self.logger.info("*************** Form Test Started *****************")
        self.driver = test_setup
        self.driver.get(FormPageLocators.FormUrl)
        self.obj = BasicForm(self.driver)
        self.obj.input_numbers(Data.get_valid_number1(), Data.get_valid_number2())
        time.sleep(2)

        self.obj.click_total_button()
        self.logger.info("**** Form Test Passed ****")

        time.sleep(3)

        self.driver.save_screenshot(".\\Screenshots\\" + "test_form.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testForm", attachment_type=AttachmentType.PNG)
        # close browser

        self.driver.close()



# pytest -v -s --alluredir=".\AllureReports" Tests\test_basic_form.py
# pytest -v --html=PytestReports\basic_form_report.html Tests\test_basic_form.py
