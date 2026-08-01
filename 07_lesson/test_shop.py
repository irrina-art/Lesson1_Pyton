from selenium import webdriver
from pages.shop_page import LoginPage
from pages.shop_page import MainPage
from pages.shop_page import CartPage
from pages.shop_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    driver.get(
       "https://www.saucedemo.com/")
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Irina", "Shilova", "630075")
    checkout_page.verify_total("58.29")

    driver.quit()
