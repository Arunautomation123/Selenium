from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

service_obj = Service(executable_path=r'D:\Projects\driver\chromedriver.exe')

driver = webdriver.Chrome(service=service_obj)

driver.get('https://practicetestautomation.com/practice-test-login/')

driver.maximize_window()
time.sleep(10)

driver.quit()
