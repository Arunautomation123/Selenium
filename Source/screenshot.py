from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://text-compare.com/')

driver.maximize_window()

driver.save_screenshot(os.getcwd() + '/homepage.png')
driver.get_screenshot_as_file(os.getcwd() + '/homepage.png')

# driver.get_screenshot_as_base64()
# driver.get_screenshot_as_png()


# how to open clicked link in new tab
reg_link = Keys.CONTROL+Keys.RETURN

driver.find_element().send_keys(reg_link)

## new tab in Selenium 4
driver.get('https://text-compare.com/')
# driver.switch_to.new_window('tab')
# driver.switch_to.new_window('window')
driver.get('https://openhrm.com/')
driver.quit()