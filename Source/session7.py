from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

# click all check boxes
ele = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and contains(@id, 'day')]")
print(len(ele))
for el in ele:
    print(el.get_attribute('id'))
    el.click()
    time.sleep(0.5)

# select checkbox based on condition
# for el in ele:
#     if el.get_attribute('id') == 'monday' or el.get_attribute('id') == 'friday':
#         el.click()


# select last two checkboxes
# for el in ele[5:]:
#     print(el.get_attribute('id'))
#     el.click()


# clear all check boxes
for el in ele:
    print(el.get_attribute('id'))
    if el.is_selected():
        el.click()
        time.sleep(0.5)
    else:
        print("check box not sleected")

time.sleep(10)
# driver.quit()