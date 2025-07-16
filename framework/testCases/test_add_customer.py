import string

from pageobjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from pageobjects.addCustomer import AddCustomer
import random
from selenium.webdriver.common.by import By
import time
import pytest

def random_genertor(size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test_003_AddNewCustomer:
    baseurl = ReadConfig.getappurl()
    username = ReadConfig.getausername()
    password = ReadConfig.getpassword()

    logger = LogGen.logGen()
    @pytest.mark.smoke
    def test_add_customer(self, setup):
        self.driver = setup
        self.logger.info('***test_add_customer***')
        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.logger.info('***Login successful***')

        self.logger.info('*******Starting add customer test*******')

        self.addcut = AddCustomer(self.driver)
        self.addcut.click_on_custmermenu()
        self.addcut.click_custoer_submenu()

        self.addcut.click_add_new_cust()

        self.logger.info('*******Providing customer info*****')
        self.addcut.enter_email_id(random_genertor(8)+ '@email.com')
        self.addcut.enter_password('random_passwd')
        self.addcut.setFirstname('Arun')
        self.addcut.setlastname('Kumar')
        self.addcut.setcompanyname('Something')
        self.addcut.setGender('Male')
        # self.addcut.customerRoles('Guests')
        self.addcut.select_vendor('Vendor 1')
        self.addcut.setAdmincontent("This is for tetsing......")
        self.addcut.click_on_save()

        self.logger.info('******Saving customer info*******')
        self.logger.info('********Strat add customer validation****')

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text

        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info('*****Add customer test passed*****')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_add_customer.png")
            self.logger.error('*****Add customer test failed ******')

        time.sleep(10)

        self.driver.close()

        self.logger.info('******test case ended*****')


