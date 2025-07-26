from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.implicitly_wait(5)
driver.get('https://opensource-demo.orangehrmlive.com/')

driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)

driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
time.sleep(2)
# driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus']").click()
# time.sleep(2)

driver.find_element(By.XPATH, "//input[@type='file']").send_keys(r"C:\Users\Dell\OneDrive\Pictures\axes.png")

time.sleep(3)

driver.quit()



