from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *

driver = webdriver.Edge()
driver.implicitly_wait(5)
driver.get('https://demoqa.com/frames')
driver.maximize_window()

driver.switch_to.frame('frame1')

try:
    ele = driver.find_element(By.XPATH, "//iframe[@id='frame1']/descendant::*")
except NoSuchElementException:
    print("Element not found")

print("Frame text", ele.text)
time.sleep(2)


frame2  = driver.find_element(By.XPATH, "//p[normalize-space()='Child Iframe']")

driver.switch_to.frame(frame2)

frame = driver.find_element(By.XPATH, "//p[@xpath='1']")
print(frame2.text)



# driver.switch_to.frame(frame)
# try:
#     ele = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
# except NoSuchElementException:
#     print("Element not found")

# print("Second frame text", ele.text)

driver.quit()