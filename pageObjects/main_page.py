from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from keyboard import press


class MainPage:
    text_box_find_symbol_css = 'input[id="symbol-search"]'
    pick_symbol_id = 'dropdown-6594-index__0'
    button_buy_css = 'button[data-testid = "TradeButton-buy"]'
    input_quantity_css = 'input[data-testid = "trade-quantity-input"]'
    button_review_id = 'review-order-button'
    button_send_order_id = 'send-order-button'
    button_working_orders_id = 'filter-working-button'
    working_orders_cell = "//label[@data-testid = 'cell']/span"
    button_sell_xpath = '//button[text()="Sell"]'
    button_order_type_xpath = "//button[@data-testid='order-type-dropdown-value']"
    market_order_xpath = "//ul//li[text()='MARKET']"
    delta_total_xpath = "//tfoot//td[@data-column='delta']/span/span"
    all_trades_check_box_css = '[class="checkbox-container center buy"] input'
    check_box_clickable_css = '[class="checkbox-container center buy"]'
    button_collap_right_panel_css = '[class="collapsable-panel__divider right-pane-divider"]'


    def __init__(self, driver):
        self.driver = driver

    def enter_symbol(self, symbol):
        self.driver.find_element(By.CSS_SELECTOR, self.text_box_find_symbol_css).send_keys(symbol)

    def click_on_symbol(self):
        press('enter')

    def get_position_quantity(self):
        check_box = self.driver.find_element(By.CSS_SELECTOR, self.all_trades_check_box_css)
        if check_box.is_selected():
            pass
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.check_box_clickable_css).click()
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR , self.button_collap_right_panel_css)).click().perform()
        total = self.driver.find_element(By.XPATH, self.delta_total_xpath).text
        return total


    def click_buy_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_buy_css).click()

    def enter_quantity(self, quantity):
        quantity_field = self.driver.find_element(By.CSS_SELECTOR, self.input_quantity_css)
        quantity_field.click()
        quantity_field.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
        self.driver.find_element(By.CSS_SELECTOR, self.input_quantity_css).send_keys(quantity)


    def click_review_button(self):
        self.driver.find_element(By.ID, self.button_review_id).click()

    def click_send_order_button(self):
        self.driver.find_element(By.ID, self.button_send_order_id).click()

    def click_working_orders(self):
        self.driver.find_element(By.ID, self.button_working_orders_id).click()

    def get_working_orders_list(self):
        items =[]
        list = self.driver.find_elements(By.XPATH,self.working_orders_cell)
        for i in list:
            items.append(i.text)
        return items

    def click_sell_button(self):
        self.driver.find_element(By.XPATH,self.button_sell_xpath).click()

    def click_order_type_button(self):
        self.driver.find_element(By.XPATH,self.button_order_type_xpath).click()

    def chose_market_order_type(self):
        self.driver.find_element(By.XPATH,self.market_order_xpath).click()



