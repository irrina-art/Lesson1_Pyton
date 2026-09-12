import pytest
from selenium import webdriver

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
          "ui: mark test as UI automation"
          )




@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    yield driver
    driver.quit()
