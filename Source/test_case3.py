from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
# used to maximize the browser window
driver.maximize_window()
# find element by link text/partial link text
# driver.find_element(By.LINK_TEXT, "Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Reg").click()


# if find element is used it returns the first matching element
# class_ele = driver.find_elements(By.CLASS_NAME, "class_name")
# print(len(class_ele))

tag_ele = driver.find_elements(By.TAG_NAME, "a")
print(len(tag_ele))
# total number of links in webpage


# input("solve captcha")


# quit will close all the browsers
driver.quit()