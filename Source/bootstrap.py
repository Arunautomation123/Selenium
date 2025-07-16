from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Edge()

driver.implicitly_wait(5)

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

cntrs = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-container']/li")

for cn in cntrs:
    if cn.text=='India':
        cn.click()

