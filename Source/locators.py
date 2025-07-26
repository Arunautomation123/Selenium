from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()
# driver.get('https://demo.nopcommerce.com/')
# used to maximize the browser window

# driver.get('https://www.facebook.com/')

# driver.maximize_window()

# CSS selector
# Tag and ID - tagname#valueofId - input#user

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys('abc@gmail.com')


# Tag and Class - tagname.classvalue

# driver.find_element(By.CSS_SELECTOR, "input.inputtext _55r1 _6luy").send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys('abc@gmail.com')
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys('abc@gmail.com')
# input.inputtext _55r1 _6luy value aftre the space is not considered

# Tag and attribute(need not be locator) - tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal-email]").send_keys('abc@gmail.com')

# Tag,class attribute - tagname.valeuofClass[attribute=value] - when tagname and classname are same
# when you want to second element

# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal-pass]").send_keys('password')


 ##### difference between find element and find elements ########


driver= webdriver.Edge()
driver.get('https://demo.nopcommerce.com/')
#1) Locator finding single elemnt
# ele = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# ele.send_keys('Samsung')

#2) locator finding mulitple web elements

# ele = driver.find_element(By.XPATH, "//div[@class='footer']//a")
# print(ele.text)

#3) element not find - nosuch element exception




#1) Locator finding single elemnt
# ele = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# # find elements returns list of objects
# ele[0].send_keys('Samsung')

#2) locator finding mulitple web elements

# ele = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
# for i in range(len(ele)):
#     print(ele[i].text)

#3) element not find - nosuch element exception is thrown in findelements
ele = driver.find_elements(By.LINK_TEXT, "Log")
print(ele)
print(len(ele))
