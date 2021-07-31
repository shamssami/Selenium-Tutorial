import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.list_box import ListBoxPage
from Utils.locators import ListBoxLocators
import time
from Utils.Logger import Logging


@allure.severity(allure.severity_level.NORMAL)
class Test_ListBox:
    logger = Logging.loggen()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_first_list_picker(self, test_setup):
        self.driver = test_setup
        self.driver.get(ListBoxLocators.ListBoxUrl)

        self.obj = ListBoxPage(self.driver)
        self.logger.info("*************** Test_001_List_Box *****************")

        # get the web page
        self.logger.info("*************** List Box1 Test Started *****************")

        self.obj.pick_value_by_index_list1(2)
        self.obj.click_add_button()
        time.sleep(2)
        # add multi elements to other list
        self.obj.pick_value_by_index_list1(1)
        self.obj.pick_value_by_index_list1(2)
        self.obj.pick_value_by_index_list1(3)
        self.obj.pick_value_by_index_list1(4)
        self.obj.click_add_button()
        time.sleep(2)
        self.obj.click_remove_all_button()
        self.obj.click_add_all_button()

        self.logger.info("**** List Box1 Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\" + "list_box1.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testListBox1",
                      attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_second_list_picker(self, test_setup):
        time.sleep(5)
        self.driver = test_setup
        self.driver.get(ListBoxLocators.ListBoxUrl)

        self.obj = ListBoxPage(self.driver)
        self.logger.info("*************** Test_002_List_Box *****************")

        # get the web page
        self.logger.info("*************** List Box2 Test Started *****************")
        self.obj.click_add_all_button()
        self.obj.pick_value_by_index_list2(2)
        # remove the selected element

        self.obj.click_remove_button()
        time.sleep(2)
        self.obj.pick_value_by_index_list2(1)
        self.obj.pick_value_by_index_list2(2)
        self.obj.pick_value_by_index_list2(3)
        self.obj.pick_value_by_index_list2(4)
        self.obj.click_remove_button()
        time.sleep(2)

        self.logger.info("**** List Box2 Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\" + "list_box2.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testListBox2",
                      attachment_type=AttachmentType.PNG)
        # close browser
        self.driver.close()

# pytest -v -s --alluredir=".\AllureReports\ListBox" Tests\test_list_box.py
# pytest -v --html=PytestReports\listBox_report.html Tests\test_list_box.py
