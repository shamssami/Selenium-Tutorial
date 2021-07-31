
from Pages.base_page import BasePage
from Utils.locators import *


class ListFilterPage(BasePage):

    def __init__(self, driver):
        self.locator = ListFilterLocators
        super().__init__(driver)

    def input_search(self, text):
        self.driver.find_element(*self.locator.input_search).send_keys(text)

    def clear_input(self):
        self.driver.find_element(*self.locator.input_search).clear()