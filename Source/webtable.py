from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Edge()
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()

###1. Count number of rows and columns###
# //table[@name='BookTable']//tbody//tr
# le = driver.find_elements(By.XPATH, "//table[@name='BookTable']//child::tr")
# print("Number of rows", len(le))

# li = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]//th")
# print("Number of columns", len(li))

# ## find element row and column

# t = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]//td[1]")
# print(t.text)

## read all rows and columns data ###

# for i in range(2, len(le)+1):
#     for j in range(1, len(li)+1):
#         txt = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tr[{str(i)}]//td[{str(j)}]")
#         print("Row: column data", txt.text, end=" ")

#     print(" ")


## read data based on conditions
# for i in range(2, len(le)+1):
#     txt = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tbody//tr[{str(i)}//td[2]]")
#     if txt.text == 'Mukesh':
#         auth = driver.find_element(By.XPATH, f"//table[@name='BookTable']//tbody//tr[{str(i)}//td[1]]")
#         print("Mukesh author book name", auth.text)

driver = webdriver.Edge()

driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()

le = driver.find_elements(By.XPATH, "//table[@id='taskTable']/tbody/tr")

for i in range(1, len(le)+1):
    tx = driver.find_element(By.XPATH, "//table[@id='taskTable']/tbody/tr[1]/td[5]")
    # if tx.text == 
