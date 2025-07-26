from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import *

driver = webdriver.Edge()

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

eles = driver.find_elements(By.XPATH, "//table[@id='taskTable']//th")
print(f"Total number of columns: {len(eles)}")

for ele in eles:
    print("Column name", ele.text)

eles_r = driver.find_elements(By.XPATH, "//table[@id='taskTable']//tbody//tr")
print(f"Total number of rows: {len(eles_r)}")

# for i in range(1, len(eles_r)+1):
#     for j in range(1, len(eles)+1):
#         ele = driver.find_element(By.XPATH, f"//table[@id='taskTable']//tbody//tr[{i}]//td[{j}]")
#         print("Element", ele.text)

for i in range(1, len(eles_r)+1):
    ele_new = driver.find_element(By.XPATH, f"//table[@id='taskTable']//tbody//tr[{i}]//td[4]")
    brow = driver.find_element(By.XPATH, f"//table[@id='taskTable']//tbody//tr[{i}]//td[1]")
    if int(ele_new.text) > 5:
        print(f"browser {brow.text} load higher: {ele_new.text}")

driver.quit()