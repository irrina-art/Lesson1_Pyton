from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 45)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

    def set_delay(self, delay_time):
        delay_field = self.driver.find_element(By.ID, "delay")
        delay_field.clear()
        delay_field.send_keys(delay_time)

    def click_button(self, button_value):
        xpath = f"//span[text()='{button_value}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self):
        result = self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
        return result.text
