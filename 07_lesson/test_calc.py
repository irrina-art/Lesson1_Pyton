from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.calculator_page import CalculatorPage


def test_calc():
    driver = webdriver.Chrome()
    driver.get(
       "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
       )
    driver.maximize_window()

    calc_page = CalculatorPage(driver)

    calc_page.set_delay("45")
    WebDriverWait(driver, 30)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    WebDriverWait(driver, 45)
    result_text = calc_page.get_result()
    assert result_text == "15"

    driver.quit()
