from selenium import webdriver
from selenium.webdriver.common.by import By


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay_time):
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(delay_time)

    def click_button(self, button_value):
        xpath = f"//span[text()='{button_value}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self):
        result_field = self.driver.find_element(By.ID, "result")
        return result_field.text
