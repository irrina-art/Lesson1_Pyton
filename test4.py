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

     
    task = driver.find_element(By.XPATH, "//div[text()='Мессенджер']")
    task.click()


    sun = driver.find_element(By.XPATH, "//div[text()='Общий чат компании']")
    sun.click()
    

    icon = driver.find_element(By.CSS_SELECTOR, "[data-testid='edit-group-chat']")
    icon.click()
    title = driver.find_element(By.XPATH, "//input[@placeholder='Введите название группового чата']")
    title.clear()
    new_title = driver.find_element(By.XPATH, "//input[@placeholder='Введите название группового чата']")
    new_title.send_keys("рабочий чат")
    chat_title = driver.find_element(By.XPATH, "//input[@value='рабочий чат']")
    title_value = chat_title.get_attribute('value')
    expected_name = "рабочий чат"
    assert title_value == expected_name

    driver.find_element (By.XPATH, "//span[contains(text(), 'Сохранить')]").click()
   
    


    