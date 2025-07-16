# browser will remember browsing data
# check whteher application creates cookies or not
# get data from cookies
# create cookies, delete cookies

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

cookies = driver.get_cookies() # captures cookies from the browser, created dynamically
# cookie has name, value, data - different attributes
print("Total cookies", len(cookies))

for cook in cookies:
    print("Cookie", cook.get('name'))

driver.quit()