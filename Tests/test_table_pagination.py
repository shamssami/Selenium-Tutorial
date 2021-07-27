from Pages.table_pagination import TablePagination
from Utils.locators import TablePaginationLocators

import setup
import time


class TestTablePagination:
    driver = setup.setup()
    obj = TablePagination(driver)

    def test_table_pagination(self):
        # open the driver
        # get the web page
        self.obj.open(TablePaginationLocators.TablePaginationUrl)
        time.sleep(3)
        # test form
        total_rows = self.obj.check_records_total_num()
        page1_rows = self.obj.check_page1_rows_number()
        page2_rows = self.obj.check_page2_rows_number()
        page3_rows = self.obj.check_page3_rows_number()

        print("Total Records is ", total_rows)
        print("Records Number in Page 1 is ", page1_rows)
        print("Records Number in Page 2 is ", page2_rows)
        print("Records Number in Page 3 is ", page3_rows)

    def test_navigation_buttons(self):
        self.obj.navigate_buttons()

        # close browser
        setup.close()


# automate this testm,,,,,,
test = TestTablePagination()
test.test_table_pagination()
test.test_navigation_buttons()
