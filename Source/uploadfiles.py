from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://www.ilovepdf.com/pdf_to_word')
driver.maximize_window()

driver.find_element(By.XPATH, "//span[normalize-space()='Select PDF file']").click().send_keys('C:\Users\Dell\Downloads\Arun_kumar_y_resume_python_automation_test.pdf')
time.sleep(2)


# selenium is not recommded for automating uploading and downloading files

# orabge hrm demo PIM/add e
driver.quit()