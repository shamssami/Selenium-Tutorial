import time

from selenium.webdriver import ActionChains

from Pages.base_page import BasePage
from Utils.locators import *


class DragDropPage(BasePage):

    def __init__(self, driver):
        self.locator = DragDropLocators
        super().__init__(driver)

    def drag_and_drop(self):
        self.driver.find_element(*self.locator.item_to_drag).click()
        source = self.driver.find_element(*self.locator.item_to_drag)
        target = self.driver.find_element(*self.locator.target)

        # action chain object creation
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        time.sleep(3)
        