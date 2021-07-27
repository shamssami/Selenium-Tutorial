from Pages.table_filter_search import TableSearch
from Utils.locators import TableSearchLocators
from Utils.test_data import TableSearchData
import setup
import time


class TestTableSearch:
    driver = setup.setup()
    obj = TableSearch(driver)

    def test_table_search(self):
        # open the driver
        # get the web page
        self.obj.open(TableSearchLocators.TableSearchUrl)
        time.sleep(3)
        # test form
        self.obj.filter_table(TableSearchData.get_task())
        time.sleep(2)
        self.obj.clear_text_field()

        self.obj.filter_table(TableSearchData.get_assignee())
        time.sleep(2)
        self.obj.clear_text_field()

        self.obj.filter_table(TableSearchData.get_status())
        time.sleep(2)
        self.obj.clear_text_field()

        time.sleep(3)

        # close browser

    def test_table_filter(self):
        # open the driver
        # get the web page
        time.sleep(3)
        # test form
        disabled_value = self.obj.is_enabled_filter()
        self.obj.click_filter_button()
        enabled_value = self.obj.is_enabled_filter()
        time.sleep(2)

        if disabled_value is False:
            print("Test Passed")
        else:
            print("Test Fail, The field should be disabled")

        if enabled_value is True:
            print("Test Passed")
        else:
            print("Test Failed, The field should be enabled")

        # close browser
        self.driver.close()


# automate this test
test = TestTableSearch()
test.test_table_search()
test.test_table_filter()
