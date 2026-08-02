from selenium import webdriver
from pages.shop_page import LoginPage
from pages.shop_page import MainPage
from pages.shop_page import CartPage
from pages.shop_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    url = "https://www.saucedemo.com/"

    login_page = LoginPage(driver, url)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.button_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Irina", "Shilova", "630075")
    checkout_page.verify_total("58.29")

    driver.quit()
