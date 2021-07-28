import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.modals import ModalsPage
from Utils.Logger import Logging
from Utils.locators import ModalsLocators
import time


@allure.severity(allure.severity_level.NORMAL)
class Test_Modals:
    logger = Logging.loggen()
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")
    obj = ModalsPage(driver)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_single_modal(self):
        self.logger.info("*************** Test_001_Single_Modal *****************")

        self.obj.open(ModalsLocators.ModalUrl)
        self.logger.info("*************** Test Single Modal Strarted *****************")

        self.obj.launch_single_modal()
        self.logger.info("Title of single modal:   "+ self.obj.get_single_modal_body())
        self.obj.get_single_modal_body()
        self.obj.click_save_single_modal()
        self.logger.info("*************** Test Single Modal Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "single_modal.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="single_modal", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_multi_modals_case1(self):
        self.logger.info("*************** Test_002_Multiple_Modal *****************")

        self.logger.info("*************** Test Multiple Modals Case1 Started *****************")

        self.obj.launch_first_multi_modals()
        time.sleep(2)
        self.logger.info("Title of first modal | case1:   "+ self.obj.get_first_multi_modal_body())
        time.sleep(2)

        self.obj.launch_second_modal()
        time.sleep(2)

        self.logger.info("Title of second modal | case1:   "+ self.obj.get_second_modal_title())
        time.sleep(2)

        self.obj.click_save_modal2_button()
        time.sleep(2)
        self.logger.info("*************** Test Multiple Modals Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "multi_modals_case1.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="multi_modals_case1",
                      attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_multi_modals_case2(self):
        self.logger.info("*************** Test_003_Multiple_Modal *****************")

        self.logger.info("*************** Test Multiple Modals Case2 Started *****************")
        self.obj.launch_first_multi_modals()
        time.sleep(2)

        self.logger.info("Title of first modal | case2:   " + self.obj.get_first_multi_modal_body())
        time.sleep(2)

        self.obj.launch_second_modal()
        time.sleep(2)

        self.logger.info("Title of Second modal | case2:   " + self.obj.get_second_modal_title())
        time.sleep(2)

        self.obj.click_close_modal2_button()
        time.sleep(2)

        self.obj.click_save_modal1_button()
        time.sleep(2)
        self.driver.save_screenshot(".\\screenshots\\" + "multi_modals_case2.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="multi_modals_case2",
                      attachment_type=AttachmentType.PNG)

        self.driver.close()

# pytest -v -s --alluredir=".\AllureReports\Modals" Tests\test_modals.py
# pytest -v --html=PytestReports\modals_report.html Tests\test_modals.py
