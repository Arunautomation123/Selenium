from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()

driver.implicitly_wait(5)

driver.get('https://text-compare.com/')

driver.maximize_window()

driver.find_element(By.XPATH, "//textarea[@id='inputText1']").send_keys('Welcome')

driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

act = ActionChains(driver)

### input select the text - Ctrl A

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

time.sleep(2)

## Ctrl + c

act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(2)

## Press tab key to naigate to 2 box

act.send_keys(Keys.TAB).perform()
time.sleep(2)

## Ctrl p

act.key_down(Keys.CONTROL).send_keys("p").key_up(Keys.CONTROL).perform()
time.sleep(3)

driver.quit()