from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageobjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
from Utilities import XLutils
import time
import pytest

# from configtest import setup

class Test_002_DDT_Login:
    baseurl = ReadConfig.getappurl()
    path = ".//TestData/test_data_2.xlsx"
    username = ReadConfig.getausername()
    password = ReadConfig.getpassword()

    logger = LogGen.logGen()
    status = []

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.driver = setup
        self.logger.info("*******Test_002_DDT_Login********")
        self.logger.info("*******test_login_ddt********")

        self.lp = Login(self.driver)

        row_cnt = XLutils.getRowcnt(self.path, 'Sheet1')
        col_cnt = XLutils.getColcnt(self.path, 'Sheet1')
        print(f"No of rows: {row_cnt}, no of columns: {col_cnt}")

        for r in range(2, row_cnt+1):
            self.username = XLutils.read_data(self.path, 'Sheet1', r, 1)
            self.password = XLutils.read_data(self.path, 'Sheet1', r, 2)
            self.exp = XLutils.read_data(self.path, 'Sheet1', r, 3)
            self.lp.set_user_name(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()

            time.sleep(5)

            act_title = self.driver.title

            if act_title == 'Dashboard / nopCommerce administration':
                if self.exp=='Pass':
                    self.lp.click_logout()
                    self.status.append('Passed')
                    self.logger.info("*******Passed******")
            else:
                if self.exp == 'Fail':
                    self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
                    self.status.append('Passed')
                    self.logger.info("*******Failed******")

        if all(eles == 'Passed' for eles in self.status):
            self.logger.info("*******Login test passed********")
            assert True
        else:
            self.logger.warning("*******Login test failed********")
            assert False

        self.logger.warning("*******End of test_login_ddt ********")


        self.driver.close()