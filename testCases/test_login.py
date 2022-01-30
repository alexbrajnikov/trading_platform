import time

from pageObjects.login_page import LoginPage
from testCases.conftest import setup
from utilities.baseclass import BaseClass
from utilities.readproperties import Readconfig
import pytest
from selenium import webdriver


@pytest.mark.skip
class TestLogin001(BaseClass):
    url = Readconfig.GetLoginUrl()
    username = Readconfig.GetUserName()
    password = Readconfig.GetPassword()

    def test_login(self, setup):
        self.driver = setup

        self.driver.get(self.url)
        lp = LoginPage(self.driver)
        lp.enter_username(self.username)
        lp.enter_password(self.password)
        lp.click_login_button()
        title = self.driver.title
        if title == 'thinkorswim Web Login | TD Ameritrade':
            assert True
            self.driver.close()
        else:
            time.sleep(5)
            self.driver.save_screenshot('.\\Screenshots\\' + "test_login.png")
            self.driver.close()
            assert False
