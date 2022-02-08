from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome("C://Users//abrajnikov//Desktop//chromedriver.exe")
    return driver
