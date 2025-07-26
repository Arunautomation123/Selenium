# Xpath is customised locator - XML path
# It is syntax or language for finding any element on the we page using XML path expression(HTML DOM structure)
# DOM (document object model)(created by browser) when webpage is loaded is API interface provided by browser
# Xpath is an address of the element

# Types of xpath
# Absolute - /html/body/nav/div/div/div[2]/ul/li[2]/a - navigates from root tag - 
# /html/body/div/div[1]/div/div[1]/div/div[1]/img
# whcih element has ID, that is taken as first element - directly jumps to element in DOM
# Relative/partial - //*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a -  //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img
# Absolute xpath we use only tags/nodes - / q# relative path we use attributes - //

# write xpath manually - absolute
#/html/body/div/div[1]/div/div[1]/div/div[1]/img - /html/body/div/div[1]/div/div[1]/div/div[1]/img
# //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img - //*[@id="app"]/div[1]/div/div[1]/div/div[1]/img
# if tagname is not known, use *

# how to capture xpath automatically - firebug, firepath - not available
# SelectorsHub - add extension to the browser - relative xpath id more stable in finding element

# absoulte xpath is not stable
# if new element are added then absolute xpath will change
# if developer changed the location then absolute path will be broken

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://magento.softwaretestingboard.com/')
driver.maximize_window()

# driver.find_element(By.XPATH, "//input[@id='search']").send_keys('pant')
driver.find_element(By.XPATH, "//input[@id='search' or @name='a']").send_keys('pant')
driver.find_element(By.XPATH, "//input[@id='search' and @name='q']").send_keys('pant')
driver.find_element(By.XPATH, "//button[@title='Search' ]").click()

# //*[contains(@id, 'mtach')]
# //*[starts-with(@id, 'st')]
# //a[text()="Man"]
time.sleep(5)

driver.quit()

# xpath axes

# self, parent, child, ancestor, descendant, following(sibling), preceding(sibling)