import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from Pages.progress_bars import ProgressBars
from Utils.Logger import Logging
from Utils.locators import ProgressBarsLocators
import time


@allure.severity(allure.severity_level.NORMAL)
class TestProgressBars:
    logger = Logging.loggen()
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")
    obj = ProgressBars(driver)

    @allure.severity(allure.severity_level.BLOCKER)
    def test_download_dialog(self):
        self.logger.info("*************** Test_001_Progress_Bars *****************")
        self.logger.info("*************** Test Download Dialog Started *****************")

        self.obj.open(ProgressBarsLocators.JqueryProgressUrl)
        self.obj.click_button_download_dialog()
        time.sleep(5)
        status = self.obj.current_percent()

        if status is True:
            self.logger.info("The progress label is dispalyed")

        self.logger.info("*************** Test Download Dialog Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "download_dialog.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="download_dialog", attachment_type=AttachmentType.PNG)


    @allure.severity(allure.severity_level.BLOCKER)
    def test_progress_circle(self):
        self.logger.info("*************** Test_002_Progress_Bars *****************")
        self.logger.info("*************** Test Download Progress Started *****************")
        self.obj.open(ProgressBarsLocators.BootstrapProgressUrl)
        self.obj.click_download_circle_button()
        time.sleep(5)
        status = self.obj.progress_percentage()
        if status is True:
            self.logger.info("The progress percent is dispalyed")

        self.logger.info("*************** Test Download Progress Finished *****************")
        self.driver.save_screenshot(".\\screenshots\\" + "download_progress.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="download_progress", attachment_type=AttachmentType.PNG)
        self.driver.close()


# pytest -v -s --alluredir=".\AllureReports\ProgressBars" Tests\test_progress_bars.py
# pytest -v --html=PytestReports\progress_bars_report.html Tests\test_progress_bars.py
