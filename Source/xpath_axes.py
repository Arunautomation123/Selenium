from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()


driver.get('https://money.rediff.com/gainers/nse/daily/groupall')
driver.maximize_window()

ele =driver.find_element(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/self::a").text
print(f"self: {ele}")
ele1 =driver.find_element(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/parent::td").text
# ele1 = driver.find_element(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/following-sibling::a[contains(text(), 'Buy')]").text
# ele2 = driver.find_element(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/following-sibling::a[contains(text(), 'Sell')]").text
print(f"Parent: {ele1}")

ele2 =driver.find_elements(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/ancestor::tr/child::td")
print(f"Child: {len(ele2)}")

ele3 =driver.find_element(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/ancestor::tr").text
print(f"ancestor: {ele3}")

ele4 =driver.find_elements(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/ancestor::tr/descendant::*")
print(ele4)

ele4 =driver.find_elements(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/ancestor::tr/following::*")

ele4 =driver.find_elements(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/ancestor::tr/preceding::*")

ele4 =driver.find_elements(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/ancestor::tr/preceding-sibling::*")
# ele1 =driver.find_element(By.XPATH, "//a[contains(text(), 'HDFC Bank')]/child::td").text
# //a[normalize-space()='HDFC Bank']
# time.sleep(5)
driver.close()