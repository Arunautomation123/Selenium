from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@given(u'launch chrome browser')
def Launchbrowser(context):
    serv_obj = Service(executable_path='D:\Projects\driver\chromedriver.exe')
    context.driver = webdriver.Chrome(service=serv_obj)
    context.driver.implicitly_wait(5)

@when(u'open orange hrm homepage')
def openHomepage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@then(u'verify that the logo present on page')
def verifyLogo(context):
    st = context.driver.find_element(By.XPATH, "//div[@class='orangehrm-login-slot-wrapper']").is_displayed()
    assert st is True

@then(u'close browser')
def close_browser(context):
    context.driver.close()