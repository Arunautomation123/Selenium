import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# background is used when multiple scenarios share common steps

@given(u'launch my chrome browser')
def Launchbrowser(context):
    serv_obj = Service(executable_path='D:\Projects\driver\chromedriver.exe')
    context.driver = webdriver.Chrome(service=serv_obj)
    context.driver.implicitly_wait(5)

@when(u'I open orange hrm homepage')
def openHomepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@when(u'Enter valid username and password')
def enter_details(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')

@when(u'click on Login')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

@then(u'user login into to dashboard page')
def verifyLogo(context):
    st = context.driver.title
    time.sleep(5)
    print(f"Page title: {st}")
    if st == "OrangeHRM":
        assert True, "Test passed"
    else:
        assert False, "Test failed"

@then(u'navigate to advanced search page')
def close_browser(context):
    context.driver.close()

@then(u'nadvanced search page should display')
def close_browser(context):
    context.driver.close()