from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    text_box_username_id='Email'
    text_box_password_id='Password'
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def set_user_name(self, username):
        self.driver.find_element(By.ID, self.text_box_username_id).clear()
        self.driver.find_element(By.ID,self.text_box_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID,self.text_box_password_id).clear()
        self.driver.find_element(By.ID,self.text_box_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

