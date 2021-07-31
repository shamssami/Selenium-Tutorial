from selenium.webdriver.support.select import Select

from Pages.base_page import BasePage
from Utils.locators import *


class ListBoxPage(BasePage):
    def __init__(self, driver):
        self.locator = ListBoxLocators
        super().__init__(driver)

    def pick_value_by_index_list1(self, index):
        selections = self.driver.find_element(*self.locator.list1_selections)
        list_values = Select(selections)
        list_values.select_by_index(index)

    def pick_value_by_index_list2(self, index):
        selections = self.driver.find_element(*self.locator.list2_selections)
        list_values = Select(selections)
        list_values.select_by_index(index)

    def click_add_button(self):
        self.driver.find_element(*self.locator.add_button).click()

    def click_add_all_button(self):
        self.driver.find_element(*self.locator.addAll_button).click()

    def click_remove_all_button(self):
        self.driver.find_element(*self.locator.removeAll_button).click()

    def click_remove_button(self):
        self.driver.find_element(*self.locator.remove_button).click()

