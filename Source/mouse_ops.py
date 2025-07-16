'''
1) mouse hover
2) right click
3) double click
4) drag abd drop
'''

from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Edge()

driver.implicitly_wait(5)

# driver.get('https://opensource-demo.orangehrmlive.com/')

# driver.maximize_window()

# driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')

# driver.find_element(By.XPATH, "//button[@type='submit']").click()

# time.sleep(3)

# admin = driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']//span[1]")
# user_mgt = driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
# user = driver.find_element(By.XPATH, "//a[@role='menuitem']")

# time.sleep(3)

# act = ActionChains(driver)

# # Mouse hover

# act.move_to_element(admin).move_to_element(user_mgt).move_to_element(user).click().perform()

# time.sleep(3)


### Right click ###

# driver.get('https://swisnl.github.io/jQuery-contextMenu/demo/input.html')

# driver.maximize_window()
# button  = driver.find_element(By.XPATH, "//span[normalize-space()='right click me']")

# act = ActionChains(driver)
# act.context_click(button).perform()

# time.sleep(3)

# driver.quit()


## double click ##

# driver.get('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick')

# driver.maximize_window()

# driver.switch_to.frame('iframeResult')

# button = driver.find_element(By.XPATH, "//p[@ondblclick='myFunction()']")

# act = ActionChains(driver)

# act.double_click(button).perform()

# time.sleep(3)

# driver.quit()


##  drag and drop ##\

# driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# driver.maximize_window()

# src = driver.find_element(By.ID, 'box6')
# dest = driver.find_element(By.ID, 'box106')

# act = ActionChains(driver)

# act.drag_and_drop(src, dest).perform()

# time.sleep(2)

# driver.quit()


## slider ##
# driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
# driver.maximize_window()

# mim_ele = driver.find_element(By.XPATH, "//div[@class='price-range-block']//span[1]")

# max_le = driver.find_element(By.XPATH, "//div[@class='price-range-block']//span[2]")

# print("before moving location of slider")

# print("Min location slider", mim_ele.location)
# print("Max location slider", max_le.location)

# act = ActionChains(driver)

# act.drag_and_drop_by_offset(mim_ele, 50, 0).perform()
# time.sleep(3)
# act.drag_and_drop_by_offset(max_le, -40, 0).perform()
# time.sleep(3)

# print("after moving location of slider")

# print("Min location slider", mim_ele.location)
# print("Max location slider", max_le.location)
# driver.quit()



## scrolling ### part of browser

driver.get('https://www.countries-ofthe-world.com/all-countries.html')
driver.maximize_window()

# using javascript inbuilt fucntion

# driver.execute_script("window.scrollBy(0, 3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved", value)

# scroll until element is found
# flag = driver.find_element(By.XPATH, "//li[normalize-space()='Italy']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved", value)
# time.sleep(2)
# driver.quit()

# scroll till end, use execute script to run javascript statements
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(5)
# driver.quit()

# scroll up to starting pos
driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
time.sleep(2)
driver.quit()


