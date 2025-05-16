import json
import pytest
from pageObjects.cart import Cart
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage

test_data_path = '../data/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    homePage = HomePage(driver)
    homePage.go_to_shop_page()
    print('jake', homePage.getTitle())

    shopPage = ShopPage(driver)
    shopPage.add_product_to_cart(test_list_item['productName'])
    shopPage.go_to_cart()
    print('jake2', shopPage.getTitle())

    cart = Cart(driver)
    cart.click_checkout_button()

    checkoutPage = CheckoutPage(driver)
    checkoutPage.select_country(test_list_item['country'])
    checkoutPage.click_checkbox()
    checkoutPage.click_purchase_button()
    checkoutPage.verify_success_message()
