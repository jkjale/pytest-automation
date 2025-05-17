import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# To run tests on Firefox: pytest --browser_name=firefox

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope='function') # 'function', 'class', 'module', 'session'
def browserInstance(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        driver_path = ChromeDriverManager().install()
        service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=service)
    elif browser_name == 'firefox':
        driver_path = GeckoDriverManager().install()
        service = FirefoxService(driver_path)
        driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.wait = WebDriverWait(driver, timeout=10)
    yield driver # before test function execution
    try:
        driver.quit()
    except Exception as e:
        print(f"Error closing the browser: {e}")