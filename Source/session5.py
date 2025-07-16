# operations on webpages
# application commands
# conditional command
# browser commands
# navigational commands
# wait commands

'''application commands
get - opening the url
title - get title of the webpage
current_url - to capture the current url
page_source - get the source code of the page'''

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Edge()

# driver.get('https://opensource-demo.orangehrmlive.com/')
# print(f"title: {driver.title}")
# print(f"url :{driver.current_url}")
# # returns the source data
# src = driver.page_source
# print(f"Page source: {src}")

# with open('sample.txt', 'w') as f:
#     f.write(src)
# driver.quit()



# Conditional commands

# is_displayed() - to check if element exists(checkbox is present or not)
# is_enabled() - to check if element is enabled or not - it takes data or not
# is_selected() - if radio button is selected or not

# driver = webdriver.Edge()

# driver.get('https://demo.nopcommerce.com/register/')
# driver.maximize_window()

# # serach = driver.find_element(By.XPATH, "//inputs[@id='small-searchterms']")

# # print(f"Element is dispalyed?: {serach.is_displayed()}")
# # print(f"Element is enabled?: {serach.is_enabled()}")

# serach1 = driver.find_element(By.ID, 'gender-male')
# print(f"Element is selected?: {serach1.is_selected()}")
# serach1.click()
# print(f"Element is selected after click?: {serach1.is_selected()}")

# serach3 = driver.find_element(By.XPATH, "//input[@id='Newsletter']")
# print(f"checkbox is selected?: {serach3.is_selected()}")
# driver.quit()

# browser commands
# .quit() - will close the browser process is not running in OS, will close multiple windows
#.close() - will close the browser but the process runs in OS, will close only single window(parent window)
# close will kill the driver process in OS



# navigational commands - through driver instance
# back
# forward
# refresh

# driver = webdriver.Edge()

# driver.get('https://www.amazon.in/')

# driver.get('https://www.flipkart.com/')

# #browser remembers the apps opened
# driver.back()
# time.sleep(5)

# driver.forward()
# time.sleep(5)

# driver.refresh()
