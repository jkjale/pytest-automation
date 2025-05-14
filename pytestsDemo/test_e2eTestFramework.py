from pageObjects.cart import Cart
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.homePage import HomePage
from pageObjects.login import LoginPage
from pageObjects.shopPage import ShopPage


def test_e2e(browserInstance):
    driver = browserInstance
    # driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # loginPage = LoginPage(driver)
    # loginPage.login()

    homePage = HomePage(driver)
    homePage.go_to_shop_page()

    shopPage = ShopPage(driver)
    shopPage.add_product_to_cart('iphone x')
    shopPage.go_to_cart()

    cart = Cart(driver)
    cart.click_checkout_button()

    checkoutPage = CheckoutPage(driver)
    checkoutPage.select_country()
    checkoutPage.click_checkbox()
    checkoutPage.click_purchase_button()
    checkoutPage.verify_success_message()
