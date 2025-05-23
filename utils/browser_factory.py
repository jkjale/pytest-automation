from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import os

def get_browser(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome()
    elif browser_name == "firefox":
        return webdriver.Firefox()
    elif browser_name == "browserstack":
        from dotenv import load_dotenv
        load_dotenv()

        USERNAME = os.getenv("BROWSERSTACK_USERNAME")
        ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

        desired_caps = {
            "browser": "Chrome",
            "os": "Windows",
            "os_version": "10",
            "name": "Target Homepage Test",
            "build": "Pytest-Selenium"
        }

        return webdriver.Remote(
            command_executor=f"http://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
            desired_capabilities=desired_caps
        )
    else:
        raise Exception("Unsupported browser!")
