# open web browser
# open url - https://opensource-demo.orangehrmlive.com
# enter username
# enter password
# click on login
# Capture title of home page
# verify title of the page
# close browser
from sys import executable

# webdriver is module which is available from selenium

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

# create object for edge class
# browser class needs driver path
# driver_path = r"C:\Drivers\chromedriver-win64\chromedriver.exe"
# driver_path = r'C:\Drivers\edgedriver_win64\msedgedriver'
# service = Service(executable=driver_path)
# driver = webdriver.Edge(service=service)
# driver = webdriver.Chrome()
driver = webdriver.Edge()
# copy the drivers to Python scripts location, in this case driver location need not be passed
driver.get('https://www.saucedemo.com/', )

WebDriverWait(driver, 10).until(presence_of_element_located((By.NAME, "user-name"))).send_keys('standard_user')
WebDriverWait(driver, 10).until(presence_of_element_located((By.NAME, "password"))).send_keys('secret_sauce')
WebDriverWait(driver, 10).until(presence_of_element_located((By.ID, "login-button"))).click()
# driver.find_element(By.XPATH, "//button[text()='Login']")
# driver.find_element(By.NAME, "Login").click()
act_tile = driver.title
print(driver.title)
exp_title = 'Swag Labs'
# class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"

assert act_tile==exp_title, "Titles dont match"
# driver.find_element(By.NAME, "password").send_keys('admin123')
# driver.find_element()

# driver.quit()
# driver.close()