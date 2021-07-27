from Pages.base_page import BasePage
from Utils.locators import *


class ProgressBars(BasePage):

    def __init__(self, driver):
        self.locator = ProgressBarsLocators
        super().__init__(driver)

    def click_button_download_dialog(self):
        # Click below button to start download.
        self.driver.find_element(*self.locator.download_button).click()

    def current_percent(self):
        # Click below button to start download.
        return self.driver.find_element(*self.locator.progress_label).is_displayed()

    # These methods for another progress bar page

    def click_download_circle_button(self):
        # Click below button to start download.
        self.driver.find_element(*self.locator.circle_button).click()

    def progress_percentage(self):
        return self.driver.find_element(*self.locator.percent_field).is_displayed()
