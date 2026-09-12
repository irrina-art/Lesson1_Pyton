from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    TASK_CREATE = (By.XPATH, "//span[text()='Создать задачу']")
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 30)
    def open(self):
        self.driver.get("https://ru.yougile.com/team/settings-account")

        
    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[placeholder = 'example@mail.ru']")))
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder = 'example@mail.ru']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder = 'Введите пароль']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[role='button']").click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Мои задачи']")))

    