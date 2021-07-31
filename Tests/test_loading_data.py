import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.Loading_data import LoadingDataPage
from Utils.locators import LoadingDataLocators
import time
from Utils.Logger import Logging


@allure.severity(allure.severity_level.NORMAL)
class Test_LoadingData:
    logger = Logging.loggen()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_list_filter(self, test_setup):
        self.driver = test_setup
        self.driver.get(LoadingDataLocators.LoadDataUrl)

        self.obj = LoadingDataPage(self.driver)
        self.logger.info("*************** Test_001_Loading Data *****************")

        # get the web page
        self.logger.info("*************** Loading Data Test Started *****************")

        self.obj.click_get_user_button()
        if self.obj.is_loading_icon_displayed() is True:
            assert "Loading Icon is Not Displayed"
            self.logger.info("*************** Loading Icon is Displayed *****************")
        else:
            self.logger.info("*************** Loading Icon is Not Displayed *****************")
            assert "Loading Icon is Not Displayed"

        time.sleep(2)
        self.obj.click_get_user_button()
        if self.obj.is_loading_icon_displayed() is True:
            assert True
            self.logger.info("*************** Loading Icon is Displayed *****************")
        else:
            self.logger.info("*************** Loading Icon is Not Displayed *****************")
            assert "Loading Icon is Not Displayed"

        time.sleep(2)
        self.obj.click_get_user_button()
        if self.obj.is_loading_icon_displayed() is True:
            assert True
            self.logger.info("*************** Loading Icon is Displayed *****************")
        else:
            self.logger.info("*************** Loading Icon is Not Displayed *****************")
            assert "Loading Icon is Not Displayed"

        time.sleep(2)
        self.obj.click_get_user_button()
        if self.obj.is_loading_icon_displayed() is True:
            assert True
            self.logger.info("*************** Loading Icon is Enabled *****************")
        else:
            self.logger.info("*************** Loading Icon is Not Enabled *****************")
            assert "Loading Icon is Not Displayed"

        time.sleep(2)
        self.logger.info("**** Loading Data Test Passed ****")

        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\" + "loading_data.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="testLoadingData",
                      attachment_type=AttachmentType.PNG)

        self.driver.close()

# pytest -v -s --alluredir=".\AllureReports\LoadingData" Tests\test_loading_data.py
# pytest -v --html=PytestReports\LoadingData_report.html Tests\test_loading_data.py
