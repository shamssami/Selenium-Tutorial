import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.ListFilter import ListFilterPage
from Utils.locators import ListFilterLocators
from Utils.test_data import ListFilterData
import time
from Utils.Logger import Logging


@allure.severity(allure.severity_level.NORMAL)
class Test_ListFilter:
    logger = Logging.loggen()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_list_filter(self, test_setup):
        self.driver = test_setup
        self.driver.get(ListFilterLocators.ListFilterUrl)

        self.obj = ListFilterPage(self.driver)
        self.logger.info("*************** Test_001_List_Filter *****************")

        # get the web page
        self.logger.info("*************** List Filter Test Started *****************")

        self.obj.input_search(ListFilterData.title)
        time.sleep(2)
        self.obj.clear_input()
        self.obj.input_search(ListFilterData.email)
        time.sleep(2)

        self.obj.clear_input()

        self.obj.input_search(ListFilterData.phone_no)
        time.sleep(2)

        self.obj.clear_input()
        self.obj.input_search(ListFilterData.name)
        time.sleep(2)

        self.obj.clear_input()
        self.obj.input_search(ListFilterData.notExist_data)

        self.logger.info("**** List Filter Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\" + "list_filter.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testListFilter",
                      attachment_type=AttachmentType.PNG)

        self.driver.close()

# pytest -v -s --alluredir=".\AllureReports\ListFilter" Tests\test_list_filter.py
# pytest -v --html=PytestReports\listFilter_report.html Tests\test_list_filter.py
