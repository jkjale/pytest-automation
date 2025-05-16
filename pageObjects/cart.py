from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils


class Cart(BrowserUtils):
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-success")

    def click_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
