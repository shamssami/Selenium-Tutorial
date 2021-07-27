import time

from Pages.base_page import BasePage
from Utils.locators import *


class Alerts(BasePage):

    def __init__(self, driver):
        self.locator = AlertsLocators
        super().__init__(driver)

    def click_autoclosable_buttons(self):
        self.driver.find_element(*self.locator.autoclosable_btn_success).click()
        time.sleep(2)

        self.driver.find_element(*self.locator.autoclosable_btn_warning).click()
        time.sleep(2)

        self.driver.find_element(*self.locator.autoclosable_btn_danger).click()
        time.sleep(2)

        self.driver.find_element(*self.locator.autoclosable_btn_info).click()
        time.sleep(2)

    def is_success_message_displayed(self):
        return self.driver.find_element(*self.locator.autoclosable_btn_success).is_displayed()

    def is_warning_message_displayed(self):
        return self.driver.find_element(*self.locator.autoclosable_btn_warning).is_displayed()

    def is_danger_message_displayed(self):
        return self.driver.find_element(*self.locator.autoclosable_btn_danger).is_displayed()

    def is_info_message_displayed(self):
        return self.driver.find_element(*self.locator.autoclosable_btn_info).is_displayed()

    def click_normal_buttons(self):
        self.driver.find_element(*self.locator.normal_btn_success).click()
        time.sleep(2)
        self.driver.find_element(*self.locator.normal_btn_warning).click()
        time.sleep(2)

        self.driver.find_element(*self.locator.normal_btn_danger).click()
        time.sleep(2)

        self.driver.find_element(*self.locator.normal_btn_info).click()
        time.sleep(2)

    def click_close_buttons(self):
        buttons = self.driver.find_elements(*self.locator.close_buttons_group)
        buttons_list = list(buttons)
        for i in buttons_list:
            i.click()
            time.sleep(2)
