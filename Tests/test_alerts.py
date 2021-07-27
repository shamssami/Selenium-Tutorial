from selenium import webdriver

from Pages.alerts import Alerts
from Utils.locators import AlertsLocators
import setup
import time


class TestAlerts:
    driver =setup.setup()
    obj = Alerts(driver)

    def test_autoclosable_alerts(self):
        self.obj.open(AlertsLocators.AlertsUrl)
        time.sleep(5)
        self.obj.click_autoclosable_buttons()
        # check if autoclosable buttons are displayed
        status1 = self.obj.is_success_message_displayed()
        status2 = self.obj.is_warning_message_displayed()
        status3 = self.obj.is_danger_message_displayed()
        status4 = self.obj.is_info_message_displayed()

        if status1 and status2 and status3 and status4 is True:
            print("Auto closableButtons Pass")

        time.sleep(7)

        if status1 and status2 and status3 and status4 is False:
            print("Auto closableButtons Pass")

    def test_normal_alerts(self):
        self.obj.click_normal_buttons()
        self.obj.click_close_buttons()
        print("Normal Alerts test Pass")
        self.driver.close()


test = TestAlerts()
test.test_autoclosable_alerts()
test.test_normal_alerts()
