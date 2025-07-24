import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given(u'i launch my chrome browser')
def Launchbrowser(context):
    serv_obj = Service(executable_path='D:\Projects\driver\chromedriver.exe')
    context.driver = webdriver.Chrome(service=serv_obj)
    context.driver.implicitly_wait(5)

@when(u'I opened orange hrm homepage')
def openHomepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@when(u'Enter username "{user}" and password "{pwd}"')
def enter_details(context, user, pwd):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)
    print(f"User name: {user}, password: {pwd}")

@when(u'click on login button')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

@then(u'user login into to the dashboard page')
def verifyLogo(context):
    st = context.driver.title
    time.sleep(5)
    print(f"Page title: {st}")
    if st == "OrangeHRM":
        assert True, "Test passed"
    else:
        assert False, "Test failed"

@then(u'close my chr browser')
def close_browser(context):
    context.driver.close()