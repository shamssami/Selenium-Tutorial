from Pages.base_page import BasePage
from Utils.locators import *


class TableSearch(BasePage):

    def __init__(self, driver):
        self.locator = TableSearchLocators
        super().__init__(driver)

    def filter_table(self, text):
        self.driver.find_element(*self.locator.input_filter_field).send_keys(text)

    def clear_text_field(self):
        self.driver.find_element(*self.locator.input_filter_field).clear()

    def is_enabled_filter(self):
        status = self.driver.find_element(*self.locator.input_data_field).is_enabled()
        return status

    def click_filter_button(self):
        self.driver.find_element(*self.locator.filter_activate_button).click()
