from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageobjects.LoginPage import Login
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import LogGen
import pytest
# from configtest import setup

class Test_001_Login:
    baseurl = ReadConfig.getappurl()
    username = ReadConfig.getausername()
    password = ReadConfig.getpassword()

    logger = LogGen.logGen()

    @pytest.mark.smoke
    def test_homepage(self, setup):
        self.logger.info("*******Test_001_Login********")
        self.logger.info("*******test_homepage********")
        self.driver = setup

        act_title = self.driver.title

        print(f"Home page title: {act_title}")

        if act_title == "nopCommerce demo store. Login":
            assert True
            self.logger.info("*******Homepage title passed********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homepage.png")
            self.logger.warning("*******Homepage title failed********")
            assert False

        self.driver.close()

    @pytest.mark.smoke
    def test_login(self, setup):
        self.driver = setup
        self.logger.info("*******test_login********")

        self.lp = Login(self.driver)
        self.lp.set_user_name(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title

        if act_title == 'Dashboard / nopCommerce administration':
            self.logger.info("*******Login test passed********")
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.logger.warning("*******Login test failed********")
            assert False

        self.driver.close()