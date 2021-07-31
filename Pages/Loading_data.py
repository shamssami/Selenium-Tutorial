from Pages.base_page import BasePage
from Utils.locators import *


class LoadingDataPage(BasePage):

    def __init__(self, driver):
        self.locator = LoadingDataLocators
        super().__init__(driver)

    def click_get_user_button(self):
        self.driver.find_element(*self.locator.get_user_button).click()

    def is_loading_icon_displayed(self):
        src = self.driver.find_element(*self.locator.loading_image).get_attribute('src')
        if "http://seleniumeasy.com/test/img/loader-image.gif" in src:
            return True


