
from Pages.basic_forms_page import BasicForm
from Utils.locators import FormPageLocators
from Utils.test_data import Data
import setup
import time


class TestForm:
    driver = setup.setup()

    def test_input_form(self):
        # open the driver
        obj = BasicForm(self.driver)
        # get the web page
        obj.open(FormPageLocators.FormUrl)
        time.sleep(3)
        # test form
        obj.input_numbers(Data.get_valid_number1(), Data.get_valid_number2())
        obj.click_total_button()

        time.sleep(3)

        # close browser
        setup.close()


# automate this test
test = TestForm()
test.test_input_form()
