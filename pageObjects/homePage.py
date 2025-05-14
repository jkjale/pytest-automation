from selenium.webdriver.common.by import By


class HomePage:
    SHOP_LINK = (By.CSS_SELECTOR, "a[href*='shop']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_shop_page(self):
        self.driver.find_element(*self.SHOP_LINK).click()
