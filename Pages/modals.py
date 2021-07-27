import time

from Pages.base_page import BasePage
from Utils.locators import *


class ModalsPage(BasePage):

    def __init__(self, driver):
        self.locator = ModalsLocators
        super().__init__(driver)

    def launch_single_modal(self):
        button = self.driver.find_element(*self.locator.launch_modal_button)
        if button.is_enabled() is True:
            time.sleep(2)
            button.click()

        else:
            print("Button is not displayedQ!")
            time.sleep(3)

    def get_single_modal_body(self):

        body = self.driver.find_element(*self.locator.single_modal_title)
        if body.is_enabled() is True:
            time.sleep(3)
            return body.text
        else:
            print("Modal body is not displayed!")

    def click_save_single_modal(self):
        button = self.driver.find_element(*self.locator.save_changes_button)

        if button.is_enabled() is True:
            time.sleep(3)
            button.click()
        else:
            print("Button is not displayed!")
            time.sleep(3)

    def launch_first_multi_modals(self):
        button = self.driver.find_element(*self.locator.launch_multi_modal_button1)
        time.sleep(3)
        if button.is_enabled() is True:
            time.sleep(3)
            button.click()
        else:
            print("Button is not displayedQ!")
            time.sleep(3)

    def get_first_multi_modal_body(self):
        time.sleep(3)
        body = self.driver.find_element(*self.locator.first_modal_title)

        if body.is_enabled() is True:
            time.sleep(3)
            return body.text
        else:
            print("Modal body is not displayedQ")

    def launch_second_modal(self):
        button = self.driver.find_element(*self.locator.launch_multi_modal_button2)
        if button.is_enabled() is True:
            time.sleep(3)
            button.click()
        else:
            print("Button is not displayedQ!")

    def get_second_modal_title(self):
        time.sleep(3)
        body = self.driver.find_element(*self.locator.second_modal_title)
        if body.is_enabled() is True:
            time.sleep(3)
            return body.text
        else:
            print("Modal body is not displayedQ")

    def click_save_modal2_button(self):
        time.sleep(3)
        button = self.driver.find_element(*self.locator.save_changes_modal2_button)
        if button.is_enabled() is True:
            time.sleep(3)
            button.click()
        else:
            print("Button is not displayedQ!")

    def click_save_modal1_button(self):
        time.sleep(3)
        button = self.driver.find_element(*self.locator.save_changes_modal1_button)
        if button.is_enabled() is True:
            time.sleep(3)
            button.click()
        else:
            print("Button is not displayed!")

    def click_close_modal2_button(self):
        time.sleep(3)
        button = self.driver.find_element(*self.locator.close_modal2_button)
        if button.is_enabled() is True:
            time.sleep(3)
            button.click()
        else:
            print("Button is not displayedQ!")

