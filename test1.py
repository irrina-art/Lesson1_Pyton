from selenium import webdriver
import os
import requests
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page import LoginPage
import pytest
import allure

load_dotenv()
@pytest.mark.ui


def test_log():
    email = os.getenv("email")
    password = os.getenv("password")
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    url = "https://ru.yougile.com/team/settings-account"
    old_url = driver.current_url

    page = LoginPage(driver, url)
    page.open()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder = 'example@mail.ru']")))
    page.login(f"{email}", f"{password}")

    new_url = driver.current_url
    assert old_url != new_url