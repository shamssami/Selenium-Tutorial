from Pages.base_page import BasePage
from Utils.locators import *


class BasicForm(BasePage):

    def __init__(self, driver):
        self.locator = FormPageLocators
        super().__init__(driver)

    def input_numbers(self, number1, number2):
        self.driver.find_element(*self.locator.NumberField1).send_keys(number1)
        self.driver.find_element(*self.locator.NumberField2).send_keys(number2)

    def click_total_button(self):
        self.driver.find_element(*self.locator.TotalButton).click()


