from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests

## links
# internal - navigate to same page - difre
# external link - different page
# broken

driver = webdriver.Edge()

# driver.get('https://demo.nopcommerce.com/')
# driver.maximize_window()


# # driver.find_element(By.LINK_TEXT, 'Digital downloads').click()
# ele = driver.find_elements(By.TAG_NAME, 'a')
# print(len(ele))

# for el in ele:
#     print("Href", el.get_attribute('href'))


##### BROKEN LINK #####
# link doesnot have target page in webserver - with error code
# developer will implement this in future
# response codes greater than 400

driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

link = driver.find_elements(By.TAG_NAME, 'a')
print("total links", len(link))
cnt = 0
for li in link:
    url = li.get_attribute('href')
    try:
        resp = requests.head(url)
    except:
        pass
    if resp.status_code >= 400:
        print("Its a broken link", url)
        cnt += 1

    else:
        print("Valid link", url)

print("Total number of broken links", cnt)