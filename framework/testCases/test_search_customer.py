import pytest

from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from pageobjects.LoginPage import Login
from pageobjects.addCustomer import AddCustomer
from pageobjects.seatchCustomer import SearchCustomer
import time

class Test_004_search_customer:
    baseurl = ReadConfig.getappurl()
    username = ReadConfig.getausername()
    password = ReadConfig.getpassword()

    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_004_search_customer_by_email(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info('***test_add_customer***')
        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.logger.info('***Login successful***')

        self.logger.info('*******Starting search customer test*******')

        self.addcut = AddCustomer(self.driver)
        self.addcut.click_on_custmermenu()
        self.addcut.click_custoer_submenu()

        self.ser_cut = SearchCustomer(self.driver)
        self.ser_cut.set_email('brenda_lindgren@nopCommerce.com')

        self.logger.info('*******Click search button*******')

        self.ser_cut.click_search_button()

        time.sleep(3)

        status = self.ser_cut.search_customer_by_email('brenda_lindgren@nopCommerce.com')

        time.sleep(10)

        if status:
            assert True
            self.logger.info('*******Customer found from email search*******')
        else:
            self.driver.save_screenshot(".\\screenshots"+"search_customer.png")
            self.logger.error('*******Customer not found from email search*******')
            assert False

        self.driver.close()

    @pytest.mark.regression
    def test_004_search_customer_by_company(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.logger.info('***test_add_customer***')
        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.logger.info('***Login successful***')

        self.logger.info('*******Starting search customer test*******')

        self.addcut = AddCustomer(self.driver)
        self.addcut.click_on_custmermenu()
        self.addcut.click_custoer_submenu()

        self.ser_cut = SearchCustomer(self.driver)
        self.ser_cut.set_company('CTS')

        self.logger.info('*******Click search button*******')

        self.ser_cut.click_search_button()

        time.sleep(3)

        status = self.ser_cut.search_customer_by_company('CTS')

        time.sleep(3)

        if status:
            assert True
            self.logger.info('*******Customer found from company search*******')
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"search_customer.png")
            self.logger.error('*******Customer not found from company search*******')
            assert False

        self.driver.close()



