from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

driver.maximize_window()
# window ID is unique everytime web browser is opened, 
# this command get ID of current window
id = driver.current_window_handle
print("ID", id)

time.sleep(5)

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

li = driver.window_handles

print("window ID", li)

driver.switch_to.window(li[1])
print("child window",driver.title)

driver.switch_to.window(li[0])
print("parent_window", driver.title)

for win_id in id:
    driver.switch_to.window(win_id)
    if driver.title == 'Orange HRM':
        driver.close()
time.sleep(5)
driver.quit()