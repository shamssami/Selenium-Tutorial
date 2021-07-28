from selenium import webdriver
import pytest


@pytest.fixture()
def test_setup():
    driver = webdriver.Chrome(executable_path="C:\\selenium\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Pytest_Reports'
    config._metadata['Module Name'] = 'Form'
    config._metadata['Tester'] = 'Shams'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
