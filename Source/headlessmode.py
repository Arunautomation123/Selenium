# testing without opening browser, test will be executed in backend
# dis-advantge normal mode - while script is running no other operation is performed
# advnatge - other task can be performed, more performance

# disadvtnage - functionalyt will not be known

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

obs = webdriver.EdgeOptions()
obs.headless=True
driver = webdriver.Edge(options=obs)
driver.get('https://demo.nopcommerce.com/')

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.maximize_window()

driver.quit()