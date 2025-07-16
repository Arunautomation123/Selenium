from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
# driver.get('https://www.tutorialspoint.com/selenium/practice/frames.php')
# driver.maximize_window()

# webelements cannot be accesed directly using find elemtn since they are part of frame
# driver.find_element(By.XPATH, "This element is in iframe - //a[normalize-space()='']//*[name()='svg']//*[name()='path'][2]").click()

# driver.find_element(By.XPATH, "//a[normalize-space()='']//*[name()='svg']").click()


# name, id and webelement
# ele = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/iframe[1]")
# driver.switch_to.frame(ele)

# driver.find_element(By.XPATH, "//a[normalize-space()='']//*[name()='svg']").click()

# go back to main page
# driver.switch_to.default_content
# switching bw frames is not possible, we need to go back to home page

# el2 = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/iframe[2]")
# driver.switch_to.frame(el2)
# driver.find_element(By.XPATH, "//a[normalize-space()='']//*[name()='svg']").click()


## INNER frames ###

##3 nested frames

driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()

driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()

outer = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer)

inner = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(inner)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys('Switched to frame')

time.sleep(5)

driver.switch_to.parent_frame() ## switch to outer frame

driver.quit()