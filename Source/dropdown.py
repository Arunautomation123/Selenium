from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# tagname of dropwdown is select

driver = webdriver.Edge()
driver.get('https://testautomationpractice.blogspot.com/')

driver.maximize_window()
# drop = driver.find_element(By.XPATH, "//select[@id='country']")

# drop_ele = Select(drop)

# these two options are available in html
# drop_ele.select_by_visible_text('India')
time.sleep(1)
# drop_ele.select_by_value("canada")
# time.sleep(2)

# select index from the dropwdown
# drop_ele.select_by_index('13')

# time.sleep(3)

# capture all options from the dropwdown

# all_opt = drop_ele.options
# for opt in all_opt:
#     print(opt.text)



# select element fro dropdown without using select
drop = driver.find_element(By.XPATH, "//select[@id='country']//child::option[@value='usa']")
drop.click()
time.sleep(3)
driver.quit()