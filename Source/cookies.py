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
    print("Cookie value", cook.get('value'))


# add new cookies to the browser
# after sdding cookie if it not added, then application is not allowing to create cookie
driver.add_cookie({"name": "new cookie", "value": "123456"})

new_size = driver.get_cookies()

print("Total cookies", len(new_size))

for cook in new_size:
    print("Cookie", cook.get('name'))


# delete a cookie from the browser - name of the cookie

driver.delete_cookie("new cookie")

new_size = driver.get_cookies()

print("Total cookies", len(new_size))


driver.delete_all_cookies()

new_size = driver.get_cookies()

print("Total cookies", len(new_size))

driver.quit()