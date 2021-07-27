from Pages.modals import ModalsPage
from Utils.locators import ModalsLocators
from Utils.test_data import Data
import setup
import time


class TestModals:
    driver = setup.setup()
    obj = ModalsPage(driver)

    def test_single_modal(self):
        self.obj.open(ModalsLocators.ModalUrl)

        self.obj.launch_single_modal()
        print("This is single modal body:   ", self.obj.get_single_modal_body())
        self.obj.get_single_modal_body()
        self.obj.click_save_single_modal()

    def test_multi_modals_case1(self):
        self.obj.launch_first_multi_modals()
        time.sleep(2)
        print("This is single modal body:   ",self.obj.get_first_multi_modal_body())
        time.sleep(2)

        self.obj.launch_second_modal()
        time.sleep(2)

        print("This is single modal body:   ",self.obj.get_second_modal_title())
        time.sleep(2)

        self.obj.click_save_modal2_button()
        time.sleep(2)


    def test_multi_modals_case2(self):
        self.obj.launch_first_multi_modals()
        time.sleep(2)

        print("This is single modal body:   ",self.obj.get_first_multi_modal_body())
        time.sleep(2)

        self.obj.launch_second_modal()
        time.sleep(2)

        print("This is single modal body:   ",self.obj.get_second_modal_title())
        time.sleep(2)

        self.obj.click_close_modal2_button()
        time.sleep(2)

        self.obj.click_save_modal1_button()
        time.sleep(2)
        self.driver.close()


test = TestModals()
test.test_single_modal()
test.test_multi_modals_case1()
test.test_multi_modals_case2()