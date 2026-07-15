from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login = driver.find_element(By.ID, "login-button")
    login.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(
        (By.NAME, "add-to-cart-sauce-labs-backpack")))

    Backpack = driver.find_element(
        By.NAME, "add-to-cart-sauce-labs-backpack")
    Backpack.click()

    shirt = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    driver.execute_script("arguments[0].click()", shirt)

    onesize = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
    driver.execute_script("arguments[0].click()", onesize)

    shopping_cart_container = driver.find_element(
        By.ID, "shopping_cart_container")
    shopping_cart_container.click()

    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    wait.until(EC.element_to_be_clickable((By.ID, 'first-name')))

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Irina")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Shilova")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("630075")

    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()

    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
    total_text = total_element.text
    print(f"Получена итоговая стоимость: {total_text}")

    expected_total = "Total: $58.29"
    assert total_text == expected_total

    driver.quit()
