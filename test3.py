from selenium import webdriver
import os
import requests
import time
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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

    page = LoginPage(driver, url)
    page.open()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder = 'example@mail.ru']")))
    page.login(f"{email}", f"{password}")

     
    driver.find_element(By.XPATH, "//div[text()='Моя компания']").click()
    driver.find_element(By.XPATH, "//span[contains(text(), 'Добавить проект')]").click()
    driver.find_element(By.XPATH, "//div[@data-testid='menu-item-add-default-project']").click()

    driver.switch_to.active_element.send_keys("очень важный проект" + Keys.ENTER)
    driver.find_element(By.XPATH, "//span[contains(text(),'Добавить задачу')]").click()
    driver.switch_to.active_element.send_keys("маленькая задачка" + Keys.ENTER)

    page_text = driver.page_source
    assert "маленькая задачка" in page_text
    
    

    