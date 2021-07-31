from Pages.drag_drop import DragDropPage
from Utils.locators import DragDropLocators
import time
from Utils.Logger import Logging

import allure
from allure_commons.types import AttachmentType


@allure.severity(allure.severity_level.NORMAL)
class Test_DragDrop:
    logger = Logging.loggen()

    ##################
    @allure.severity(allure.severity_level.BLOCKER)
    def test_drag_drop(self, test_setup):
        self.logger.info("*************** Test_001_Drag And Drop *****************")
        self.logger.info("*************** Drag & Drop Test Started *****************")
        self.driver = test_setup
        self.driver.get(DragDropLocators.DragDropUrl)
        self.obj = DragDropPage(self.driver)
        self.obj.drag_and_drop()

        self.logger.info("**** Drag & Drop Test Passed ****")

        time.sleep(3)

        self.driver.save_screenshot(".\\Screenshots\\" + "test_drag&drop.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testDrag&Drop", attachment_type=AttachmentType.PNG)
        # close browser

        self.driver.close()

# pytest -v -s --alluredir=".\AllureReports\Drag&Drop" Tests\test_drag_drop.py
# pytest -v --html=PytestReports\drag&drop_report.html Tests\test_drag_drop.py
