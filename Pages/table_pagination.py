from Pages.base_page import BasePage
from Utils.locators import *


class TablePagination(BasePage):

    def __init__(self, driver):
        self.locator = TablePaginationLocators
        super().__init__(driver)

    def check_records_total_num(self):
        rows_objects = self.driver.find_elements(*self.locator.rows)
        rows_number = len(rows_objects)
        return rows_number

    def check_page1_rows_number(self):
        self.driver.find_element(*self.locator.page_link1).click()
        rows_objects = self.driver.find_elements(*self.locator.rows)
        page1_rows = list(rows_objects)
        count = 0
        for i in page1_rows:
            if i.get_attribute("style") == "display: table-row;":
                count += 1
        return count

    def check_page2_rows_number(self):
        self.driver.find_element(*self.locator.page_link2).click()
        rows_objects = self.driver.find_elements(*self.locator.rows)
        page2_rows = list(rows_objects)
        count = 0
        for i in page2_rows:
            if i.get_attribute("style") == "display: table-row;":
                count += 1
        return count

    def check_page3_rows_number(self):
        self.driver.find_element(*self.locator.page_link3).click()
        rows_objects = self.driver.find_elements(*self.locator.rows)
        page3_rows = list(rows_objects)
        count = 0
        for i in page3_rows:
            if i.get_attribute("style") == "display: table-row;":
                count += 1
        return count

    def navigate_buttons(self):
        self.driver.find_element(*self.locator.page_link2).click()

        prev_btn_status = self.driver.find_element(*self.locator.prev_link)
        next_btn_status = self.driver.find_element(*self.locator.next_link)

        if prev_btn_status and next_btn_status is True:
            next_btn_status.click()
            prev_btn_status.click()
            prev_btn_status.click()
