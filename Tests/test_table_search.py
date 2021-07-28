import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.table_filter_search import TableSearch
from Utils.Logger import Logging
from Utils.locators import TableSearchLocators
from Utils.test_data import TableSearchData
import time


@allure.severity(allure.severity_level.NORMAL)
class TestTableSearch:
    logger = Logging.loggen()
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")
    obj = TableSearch(driver)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_table_search(self):
        self.logger.info("*************** Test_001_Table_Search *****************")

        self.logger.info("*************** Test Table Search Started *****************")

        self.obj.open(TableSearchLocators.TableSearchUrl)
        time.sleep(3)
        # test form
        self.obj.filter_table(TableSearchData.get_task())
        time.sleep(2)
        self.obj.clear_text_field()

        self.obj.filter_table(TableSearchData.get_assignee())
        time.sleep(2)
        self.obj.clear_text_field()

        self.obj.filter_table(TableSearchData.get_status())
        time.sleep(2)
        self.obj.clear_text_field()

        time.sleep(3)
        self.logger.info("*************** Test Table Search  Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "table_search.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="table_search", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_table_filter(self):
        self.logger.info("*************** Test_002_Table_Filter *****************")

        self.logger.info("*************** Test Table Filter Activation Started *****************")

        time.sleep(3)
        # check filter icon activation
        disabled_value = self.obj.is_enabled_filter()
        self.obj.click_filter_button()
        enabled_value = self.obj.is_enabled_filter()
        time.sleep(2)

        # filter table should be disabled before clicking on filter icon
        if disabled_value is False:
            self.logger.info("Passed, Filter Icon Is Disabled")
        else:
            self.logger.error("Test Failed, The field should be disabled")

        # filter table should be enabled after clicking on filter icon

        if enabled_value is True:
            self.logger.info("Passed, Filter Icon Is Enabled")
        else:
            self.logger.error("Test Failed, The field should be enabled")

        # close browser
        self.logger.info("*************** Test Table Filter Activation Buttons  Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "table_filter.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="table_filter",
                      attachment_type=AttachmentType.PNG)
        self.driver.close()

    # pytest -v -s --alluredir=".\AllureReports\TableSearch" Tests\test_table_search.py
    # pytest -v --html=PytestReports\table_search.html Tests\test_table_search.py
