from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        service_obj = Service(executable_path=r'D:\Projects\driver\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)
        print("Chrome browser launching------ ")
    elif browser == 'Edge':
        service_obj_edge = Service(executable_path=r'D:\Projects\driver\msedgedriver.exe')
        driver = webdriver.Edge(service=service_obj_edge)
        print("Edge browser launching------ ")
    else:
        print("Default browser starting -------")
        service_obj = Service(executable_path=r'D:\Projects\driver\chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)

    driver.get('https://admin-demo.nopcommerce.com/')
    driver.implicitly_wait(10)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

####### Pytest HTML report ########
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Nop commerce demo'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Arun'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
