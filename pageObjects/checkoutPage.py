from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    COUNTRY_INPUT = (By.ID, "country")
    COUNTRY_DRPDWN_SELECTION = (By.XPATH, "//a[text()='United States of America']")
    CHECKBOX = (By.CSS_SELECTOR, "[for='checkbox2']")
    PURCHASE_BUTTON = (By.CSS_SELECTOR, "[value='Purchase']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success > strong")

    def __init__(self, driver):
        self.driver = driver

    def select_country(self, country):
        country_input = self.driver.find_element(*self.COUNTRY_INPUT)
        country_input.send_keys(country)
        self.driver.wait.until(
            EC.element_to_be_clickable(self.COUNTRY_DRPDWN_SELECTION),
            message=f'Element not clickable by {self.COUNTRY_DRPDWN_SELECTION}'
        ).click()

    def click_checkbox(self):
        self.driver.find_element(*self.CHECKBOX).click()

    def click_purchase_button(self):
        self.driver.find_element(*self.PURCHASE_BUTTON).click()

    def verify_success_message(self):
        success_msg = self.driver.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE),
        )
        assert 'success!' in success_msg.text.strip().lower()