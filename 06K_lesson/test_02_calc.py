from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.get(
       "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
       )
    driver.maximize_window()

    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")
    WebDriverWait(driver, 30)
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        xpath = f"//span[text()='{button}']"
    click_button = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click()", click_button)
    WebDriverWait(driver, 40)

    result = WebDriverWait(driver, 45).until(
     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    assert result
    driver.quit()
