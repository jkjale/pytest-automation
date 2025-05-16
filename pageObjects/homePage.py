from selenium.webdriver.common.by import By

from utils.browserutils import BrowserUtils


class HomePage(BrowserUtils):
    SHOP_LINK = (By.CSS_SELECTOR, "a[href*='shop']")

    def go_to_shop_page(self):
        self.driver.find_element(*self.SHOP_LINK).click()
