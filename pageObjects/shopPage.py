from selenium.webdriver.common.by import By


class ShopPage:
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".card.h-100")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#navbarResponsive a")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name):
        products = self.driver.find_elements(*self.PRODUCT_CARDS)
        for product in products:
            if product.find_element(By.CSS_SELECTOR, "h4 a").text == product_name:
                product.find_element(By.CSS_SELECTOR, "button").click()

    def go_to_cart(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
