from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    main_customers_xpath ="//a[@href='#']//p[contains(text(),'Customers')]"
    sub_customer_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    add_new_xpath = "//a[@class='btn btn-primary']"
    text_box_email_id = 'Email'
    text_box_pwd_id = 'Password'
    text_box_first_name_id = 'FirstName'
    text_box_last_name_id = 'LastName'
    radio_button_male = "//input[@id='Gender_Male']"
    radio_button_female = "//input[@id='Gender_Female']"
    text_box_company_id = "Company"
    check_box_tax_name = "IsTaxExempt"
    dropdown_vendor_id = 'VendorId'
    input_active_id = 'MustChangePassword'
    input_cust_cng_pwd_id = 'MustChangePassword'
    text_area_id = 'AdminComment'
    save_button_xpath = "//button[@name='save']"
    li_text_administrators_xpath = "//li[@title='Administrators']"
    li_text_forum_moder_xpath = "//li[@title='Forum Moderators']"
    li_text_registered_xpath = "//li[@title='Registered']"
    li_text_guest_xpath = "//li[@title='Guests']"
    li_text_vendor_xpath = "//li[@title='Vendors']"
    customer_role_xpath = "//input[@class='select2-search__field valid']"

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def click_on_custmermenu(self):
        self.driver.find_element(By.XPATH, self.main_customers_xpath).click()

    def click_custoer_submenu(self):
        self.driver.find_element(By.XPATH, self.sub_customer_xpath).click()

    def click_add_new_cust(self):
        self.driver.find_element(By.XPATH, self.add_new_xpath).click()

    def enter_email_id(self, email):
        self.driver.find_element(By.ID, self.text_box_email_id).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.text_box_pwd_id).send_keys(password)

    def customerRoles(self, role):
        self.driver.find_element(By.XPATH, self.customer_role_xpath).click()
        time.sleep(3)

        if role == 'Registered':
            self.lstitem = self.driver.find_element(By.XPATH, self.li_text_registered_xpath)
        elif role == 'Administrators':
            self.lstitem = self.driver.find_element(By.XPATH, self.li_text_administrators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//span[@role='presentation']").click()
            self.lstitem = self.driver.find_element(By.XPATH, self.li_text_guest_xpath)
        elif role == 'Vendors':
            self.lstitem = self.driver.find_element(By.XPATH, self.li_text_vendor_xpath)
        else:
            self.lstitem = self.driver.find_element(By.XPATH, self.li_text_guest_xpath)
        time.sleep(3)
        self.lstitem.click()
        self.driver.execute_script("arguments[0].click();", self.lstitem)

    def select_vendor(self,vendor):
        ele = self.driver.find_element(By.ID, self.dropdown_vendor_id)
        element = Select(ele)
        element.select_by_visible_text(vendor)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.radio_button_male).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.radio_button_female).click()
        else:
            self.driver.find_element(By.XPATH, self.radio_button_male).click()

    def setFirstname(self, name):
        self.driver.find_element(By.ID, self.text_box_first_name_id).send_keys(name)

    def setlastname(self, name):
        self.driver.find_element(By.ID, self.text_box_last_name_id).send_keys(name)

    def setcompanyname(self, company_name):
        self.driver.find_element(By.ID, self.text_box_company_id).send_keys(company_name)

    def setAdmincontent(self, content):
        self.driver.find_element(By.ID, self.text_area_id).send_keys(content)

    def click_on_save(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

