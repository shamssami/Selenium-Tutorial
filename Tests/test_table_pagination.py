import logging

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.table_pagination import TablePagination
from Utils.Logger import Logging
from Utils.locators import TablePaginationLocators

import time

@allure.severity(allure.severity_level.NORMAL)
class TestTablePagination:
    logger = Logging.loggen()
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")
    obj = TablePagination(driver)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_table_pagination(self):
        self.logger.info("*************** Test_001_Table_Pagination *****************")

        self.logger.info("*************** Test Table Pagination Started *****************")

        self.obj.open(TablePaginationLocators.TablePaginationUrl)
        time.sleep(3)
        # test form
        total_rows = self.obj.check_records_total_num()
        page1_rows = self.obj.check_page1_rows_number()
        page2_rows = self.obj.check_page2_rows_number()
        page3_rows = self.obj.check_page3_rows_number()

        print("Total Records is ", total_rows)
        print("Records Number in Page 1 is ", page1_rows)
        print("Records Number in Page 2 is ", page2_rows)
        print("Records Number in Page 3 is ", page3_rows)

        self.logger.info("*************** Test Table Pagination Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "table_pagination.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="tabel_pagination", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_navigation_buttons(self):
        self.logger.info("*************** Test Table Navigation Buttons Started *****************")

        self.obj.navigate_buttons()

        self.logger.info("*************** Test Table Navigation Buttons  Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "table_navigation_buttons.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="table_navigation_buttons", attachment_type=AttachmentType.PNG)
        self.driver.close()

    # pytest -v -s --alluredir=".\AllureReports\TablePagination" Tests\test_table_pagination.py
    # pytest -v --html=PytestReports\table_pagination_report.html Tests\test_table_pagination.py
