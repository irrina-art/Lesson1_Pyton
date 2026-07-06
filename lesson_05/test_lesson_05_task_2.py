from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()

    driver.find_element(By.NAME, "custname").send_keys(
        "Irina"
        )
    driver.find_element(By.XPATH, "//button[text()='Submit order']"). click()

    new_url = driver.current_url
    assert new_url != "https://httpbin.org/forms/post"

    driver.quit()
