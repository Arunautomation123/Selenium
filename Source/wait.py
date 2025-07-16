###### WAIT COMMANDS######

# syncronisation problem, when application is not in sync with code

# implicit wait
# explicit wait

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


driver = webdriver.Edge()

# this statement will be applicable for all the statements below this
# No performance impact
# 10 is max timeout seconds

# if element not found within 10s - exception raised
driver.implicitly_wait(10)

### Explicit wait ####

# works based on conditions

# explciit wait declaration
# mulitple places explicit wait needs to be used
# it has exception handling
# poll frequency every second it will find elemt
expl = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, NoSuchDriverException])

driver.get('https://www.google.com/')
driver.maximize_window()

ele = driver.find_element(By.NAME, 'q')
ele.send_keys('Selenium')
ele.submit()


# webpage might be available within this time
# this reduces performance of the automation
# even after 5 seconds element cannot be found, execption can be raised
time.sleep(5)

el = driver.find_element(By.XPATH, "//h3[text()='Selenium']")
el.click()
print(driver.title())
ser = expl.until(EC.presence_of_element_located(By.XPATH, "//h3[text()='Selenium']"))
ser.click()