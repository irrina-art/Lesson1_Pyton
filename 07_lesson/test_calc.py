from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    calc_page = CalculatorPage(driver, url)
    calc_page.open()

    calc_page.set_delay("45")
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result_text = calc_page.get_result()
    assert result_text == "15"

    driver.quit()
