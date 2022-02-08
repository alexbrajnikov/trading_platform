import time
from selenium import webdriver
from pageObjects.login_page import LoginPage
from pageObjects.main_page import MainPage
from testCases.conftest import setup
from utilities.baseclass import BaseClass
from utilities.readproperties import Readconfig
import pytest
from selenium import webdriver


class TestPlacingSellOrderMarket(BaseClass):
    url = Readconfig.GetLoginUrl()
    username = Readconfig.GetUserName()
    password = Readconfig.GetPassword()
    symbol = Readconfig.get_symbol()
    quantity = Readconfig.get_quantity()

    def test_placing_sell_order_market_day(self,setup):
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
        time.sleep(3)
        mp.click_on_symbol()
        position = mp.get_position_quantity()
        mp.click_sell_button()
        mp.enter_quantity(self.quantity)
        mp.click_order_type_button()
        time.sleep(2)
        mp.chose_market_order_type()
        mp.click_review_button()
        mp.click_send_order_button()
        print(position)
        position_after_trade_exp = (float(position) - float(self.quantity))
        position_after_trade_act = mp.get_position_quantity()
        time.sleep(10)
        assert round(float(position_after_trade_act)) == round(float(position_after_trade_exp))
        self.driver.close()