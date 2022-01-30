import time
from selenium import webdriver
from pageObjects.login_page import LoginPage
from pageObjects.main_page import MainPage
from testCases.conftest import setup
from utilities.baseclass import BaseClass
from utilities.readproperties import Readconfig
import pytest
from selenium import webdriver


@pytest.mark.skip
class TestPlacingSellOrder(BaseClass):
    url = Readconfig.GetLoginUrl()
    username = Readconfig.GetUserName()
    password = Readconfig.GetPassword()
    symbol = Readconfig.get_symbol()
    quantity = Readconfig.get_quantity()

    def testing_placing_sell_order_lim(self, setup):
        self.driver = setup
        lp = LoginPage(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        lp.enter_username(self.username)
        lp.enter_password(self.password)
        lp.click_login_button()
        mp = MainPage(self.driver)
        mp.enter_symbol(self.symbol)
        mp.click_on_symbol()
        mp.click_sell_button()
        mp.enter_quantity(self.quantity)
        mp.click_review_button()
        mp.click_send_order_button()
        self.driver.close()
