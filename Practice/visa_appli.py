from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.maximize_window()
driver.implicitly_wait(10)

# cookie = driver.get_cookies()
# print("Number of cookies", len(cookie))

# driver.find_element(By.XPATH, "//span[@id='select2-billing_state-container']").click()

# eles = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_state-results']/li")

# for ele in eles:
#     if ele.text == 'Kerala':
#         ele.click()
#         break

# time.sleep(10)  


driver.find_element(By.XPATH, "//input[@id='dob']").click()

ele = driver.find_element(By.XPATH, "//select[@aria-label='Select month']")

elemnet = Select(ele)
elemnet.select_by_visible_text('Oct')

ele = driver.find_element(By.XPATH, "//select[@aria-label='Select year']")

elemnet = Select(ele)
elemnet.select_by_visible_text('1998')


days = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for day in days:
    if day.text =='22':
        day.click()
        break

time.sleep(5)
driver.quit()