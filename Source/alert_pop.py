# alert is not webelement, element cannot be identified

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


# driver = webdriver.Edge()
# driver.get('https://testpages.herokuapp.com/styled/alerts/alert-test.html')
# driver.maximize_window()

# # open alert window
# driver.find_element(By.XPATH, "//input[@id='promptexample']").click()

# time.sleep(5)

# capture the text message on alert window
# alert = driver.switch_to.alert
# print(alert.text)
# time.sleep(2)
# alert.send_keys('Enter custom text')
# alert.accept() # close the alert window

# time.sleep(2)

# close alert window by clicking cancelling
# alert.dismiss()
# time.sleep(5)

# driver.get('https://mypage.rediff.com/login/dologin')
# driver.maximize_window()

# driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(5)


#### AUTHENTICATION POP UP #####

# syntax for authentication pop-up it is bypassed
###https://username:password@text.com

# driver.get('https://admin:admin@testpages.herokuapp.com/styled/auth/basic-auth-results.html')

# driver.maximize_window()
# time.sleep(5)
# driver.quit()

### Notification pop-up ####
# comes from the browser, not from the application, this pop-up cannot be

ops = webdriver.EdgeOptions()
ops.add_argument('--disable-notifications')

driver = webdriver.Edge(options=ops)

driver.get('https://whatmylocation.com/')

driver.maximize_window()
time.sleep(5)
driver.quit()
