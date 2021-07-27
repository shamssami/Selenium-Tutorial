from Pages.input_form import InputForm
from Utils.locators import InputFormLocators
from Utils.test_data import Data
import setup
import time


class TestInputForm:
    driver = setup.setup()

    def test_input_form(self):
        # open the driver
        obj = InputForm(self.driver)
        # get the web page
        obj.open(InputFormLocators.InputFormUrl)
        time.sleep(3)
        # test form
        obj.input_data()

        count =0
        if obj.check_invalidation() is True:
            count = count+1
            print("Test Failed with ", count, "errors")

        time.sleep(3)

        # close browser
        setup.close()


# automate this test
test = TestInputForm()
test.test_input_form()
