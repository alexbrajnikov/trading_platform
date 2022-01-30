from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    textbox_username_id = 'username0'
    textbox_password_id = 'password1'
    button_login_id = 'accept'

    def __init__(self,driver):
        self.driver = driver


    def enter_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID,self.button_login_id).click()
