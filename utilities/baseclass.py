import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:


    def send_keys(self,method, locator, keys, wait_time=10):
        try:
            element = object
            wdwait = WebDriverWait(self.driver, wait_time)
            if method == 'xpath':
                element = wdwait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elif method == 'css':
                element = wdwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            elif method == 'id':
                element = wdwait.until(EC.presence_of_element_located((By.ID, locator)))
            elif method == 'name':
                element = wdwait.until(EC.presence_of_element_located((By.NAME, locator)))
            elif method == 'link':
                element = wdwait.until(EC.presence_of_element_located((By.LINK_TEXT, locator)))
            element.send_keys(keys)
        except (NoSuchElementException, TimeoutException) as err:
            print('Error on click element by locator, check locator', locator)
            print(err)

    def click_element_by_locator(self,method, locator, wait_time=10):
        """click with explicit wait"""
        try:
            wdwait = WebDriverWait(self.driver, wait_time)
            # elem = driver.find_element(xpath) - this is with implicit wait
            element = object  # very general data type
            if method == 'xpath':
                element = wdwait.until(EC.element_to_be_clickable((By.XPATH, locator)))
            elif method == 'id':
                element = wdwait.until(EC.element_to_be_clickable((By.ID, locator)))
            elif method == 'css':
                element = wdwait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            elif method == 'name':
                element = wdwait.until(EC.element_to_be_clickable((By.NAME, locator)))
            elif method == 'link':
                element = wdwait.until(EC.element_to_be_clickable((By.LINK_TEXT, locator)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            print('Error on click element by locator, check locator', locator)
            print(err)

    def select_drop_down(self,method, locator, way, value, wait_time=10):
        try:
            wdwait = WebDriverWait(self.driver, wait_time)
            # elem = driver.find_element(xpath) - this is with implicit wait
            element = object  # very general data type

            if method == 'xpath':
                element = Select(wdwait.until(EC.presence_of_element_located((By.XPATH, locator))))
            elif method == 'id':
                element = Select(wdwait.until(EC.presence_of_element_located((By.ID, locator))))
            elif method == 'css':
                element = Select(wdwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator))))
            elif method == 'name':
                element = Select(wdwait.until(EC.presence_of_element_located((By.NAME, locator))))
            if way == 'value':
                element.select_by_value(value)
            elif way == 'text':
                element.select_by_visible_text(value)
            elif way == 'index':
                element.select_by_index(value)

        except (NoSuchElementException, TimeoutException) as err:
            print('Error on click element by locator, check locator', locator)
            print(err)

    def find_elements_by_locator(self, method, locator, wait_time=10):

        """find with explicit wait"""
        try:
            wdwait = WebDriverWait(self.driver, wait_time)
            # elem = driver.find_element(xpath) - this is with implicit wait
            element = object  # very general data type
            if method == 'xpath':
                elements = wdwait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
            elif method == 'id':
                elements = wdwait.until(EC.presence_of_all_elements_located((By.ID, locator)))
            elif method == 'css':
                elements = wdwait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
            elif method == 'name':
                elements = wdwait.until(EC.presence_of_all_elements_located((By.NAME, locator)))
            elif method == 'link':
                elements = wdwait.until(EC.presence_of_element_located((By.LINK_TEXT, locator)))

            return elements
        except (NoSuchElementException, TimeoutException) as err:
            print('Error on click element by locator, check locator', locator)
            print(err)

