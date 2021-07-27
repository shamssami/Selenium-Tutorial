from Pages.progress_bars import ProgressBars
from Utils.locators import ProgressBarsLocators
from Utils.test_data import Data
import setup
import time


class TestProgressBars:
    driver = setup.setup()
    obj = ProgressBars(driver)

    def test_download_dialog(self):
        self.obj.open(ProgressBarsLocators.JqueryProgressUrl)
        self.obj.click_button_download_dialog()
        time.sleep(5)
        status = self.obj.current_percent()

        if status is True:
            print("The progress label is dispalyed")

    def test_progress_circle(self):
        self.obj.open(ProgressBarsLocators.BootstrapProgressUrl)
        self.obj.click_download_circle_button()
        time.sleep(5)
        status = self.obj.progress_percentage()
        if status is True:
            print("The progress percent is dispalyed")

        setup.close()


test = TestProgressBars()
test.test_download_dialog()
test.test_progress_circle()
