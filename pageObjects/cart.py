from selenium.webdriver.common.by import By


class Cart:
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
    