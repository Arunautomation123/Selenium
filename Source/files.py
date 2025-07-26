from selenium import webdriver
# from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os

loc = os.getcwd()
# download files in desire directory
preferences = {"download.default_directory": loc, "plugins.always_open_pdf_externally": True}
ops = webdriver.EdgeOptions()
ops.add_experimental_option("prefs", preferences)
driver = webdriver.Edge(options=ops)
driver.implicitly_wait(15)

driver.get('https://file-examples.com/index.php/sample-documents-download/')
driver.maximize_window()

# driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()


# for firefox, by default download click will download the file, we hvae to 
# set the preference 
# ops = webdriver.FurefoxOptions()
# check MIME type of file 
# ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword - /pdf") - type of file needs to be specified
# ops.set_perference("browser.download.manager.showWhenStaring", "False")
# ops.set_preference("browser.download.folderList", 2) # 0 -desktop, 1 - downloads, 2 - desired folder
# ops.set_preference("browser.download.dir", location)
# ops.set_preference("pdfjs.disabled", True)


# downloading pdf file - file is not downloaded directly

driver.find_element(By.XPATH, "//a[@href='https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/']").click()
time.sleep(3)
driver.quit()