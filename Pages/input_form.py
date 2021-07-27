from selenium.webdriver.support.select import Select

from Pages.base_page import BasePage
from Utils.locators import *
from Utils.test_data import InputFormData


class InputForm(BasePage):

    def __init__(self, driver):
        self.locator = InputFormLocators
        super().__init__(driver)

    def input_data(self):
        self.input_f_name(InputFormData.get_first_name())
        self.input_last_name(InputFormData.get_last_name())
        self.input_email(InputFormData.get_email())
        self.input_phone_no(InputFormData.get_phone_no())
        self.input_address(InputFormData.get_address())
        self.input_city(InputFormData.get_city())
        self.select_state(InputFormData.get_state_index())
        self.input_zip_code(InputFormData.get_zip_code())
        self.input_website_domain_name(InputFormData.get_website_domain_name())
        self.input_description(InputFormData.get_description())
        self.click_radio_button()

    def input_first_name(self, first_name):
        self.driver.find_element(*self.locator.first_name).send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(*self.locator.last_name).send_keys(last_name)

    def input_email(self, email):
        self.driver.find_element(*self.locator.email).send_keys(email)

    def input_phone_no(self, phone_no):
        self.driver.find_element(*self.locator.phone_no).send_keys(phone_no)

    def input_address(self, address):
        self.driver.find_element(*self.locator.address).send_keys(address)

    def input_city(self, city):
        self.driver.find_element(*self.locator.city).send_keys(city)

    def select_state(self, state_index):
        state = self.driver.find_element(*self.locator.state)
        Select(state).select_by_index(state_index)

    def input_zip_code(self, zip_code):
        self.driver.find_element(*self.locator.zip_code).send_keys(zip_code)

    def input_website_domain_name(self, website_domain_name):
        self.driver.find_element(*self.locator.website_domain_name).send_keys(website_domain_name)

    def click_radio_button(self):
        self.driver.find_element(*self.locator.radio_button).click()

    def input_description(self, description):
        self.driver.find_element(*self.locator.description).send_keys(description)

    def check_validation(self):
        status = self.driver.find_element(*self.locator.valid).is_displayed()
        return status

    def check_invalidation(self):
        status = self.driver.find_element(*self.locator.invalid).is_displayed()
        return status

    def input_f_name(self, first_name):
        self.driver.find_element(*self.locator.first_name).send_keys(first_name)
